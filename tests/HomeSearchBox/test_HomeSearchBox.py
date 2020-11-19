import time
from datetime import datetime, timedelta
import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from POM.HomeSearchBox import DateNotSelectable, HomeSearchBoxPage
from Utilities.data_fixtures import from_to_search_data, date_data, traveller_class_data, search_button_data


@pytest.mark.usefixtures("setup")
class TestHomeSearchBox:
    def test_oneway_button(self, logger, explicit_wait, top_nav, home_search_box_page):
        try:
            home_search_box_page.one_way_button().click()
            home_search_box_page.from_input_box().click()
            home_search_box_page.from_search_input_box().send_keys("ch")
            from_cities = home_search_box_page.from_dropdown_items()
            for city in from_cities:
                if "Chennai, India" in city.text:
                    city.click()
                    break
            home_search_box_page.to_input_box().click()
            home_search_box_page.to_search_input_box().send_keys("mu")
            to_cities = home_search_box_page.to_dropdown_items()
            for city in to_cities:
                if "Mumbai, India" in city.text:
                    city.click()
                    break
            one_way_class = home_search_box_page.one_way_button().get_attribute("class")
            assert one_way_class == "slt oneway"
            home_search_box_page.search_button().click()
            value = home_search_box_page.return_date_input_value().get_attribute("style")
            assert value == 'cursor: no-drop;'
            top_nav.home_link().click()

        except:
            logger.exception("")
            assert False

    def test_oneway_round_trip_button(self, logger, explicit_wait,home_search_box_page):
        try:
            home_search_box_page.round_trip_button().click()
            round_trip_class = home_search_box_page.round_trip_button().get_attribute("class")
            assert round_trip_class == "roundway slt"
            home_search_box_page.one_way_button().click()
            one_way_class = home_search_box_page.one_way_button().get_attribute("class")
            assert one_way_class == "oneway slt"
        except:
            logger.exception("")
            assert False

    def test_flight_from_search_input_box(self, explicit_wait, logger, home_search_box_page, from_to_search_data):
        try:
            self.driver.refresh()
            home_search_box_page.from_input_box().click()
            home_search_box_page.from_search_input_box().send_keys(from_to_search_data["SearchCity"])
            try:
                explicit_wait.until(expected_conditions.visibility_of_element_located(home_search_box_page.FROM_DROPDOWN_BOX_LOCATOR))
            except:
                assert int(from_to_search_data["ExpectedLen"]) == 0
                return
            from_cities = home_search_box_page.from_dropdown_items()
            assert len(from_cities) == int(from_to_search_data["ExpectedLen"])
            if len(from_cities) > 0:
                from_city = from_cities[int(from_to_search_data["CityIndexToSelect"])]
                actual_from_city_name = home_search_box_page.get_city_name(from_city)
                actual_from_city_desc = home_search_box_page.get_city_description(from_city).replace("-", ",")
                from_city.click()
                expected_city_name = home_search_box_page.from_input_box().get_attribute("value")
                expected_city_desc = home_search_box_page.depart_airport().text
                assert actual_from_city_desc == expected_city_desc
                assert expected_city_name in actual_from_city_name
        except:
            logger.exception("")
            assert False

    def test_flight_to_input_search_box(self, logger, home_search_box_page, from_to_search_data, explicit_wait):
        try:
            self.driver.refresh()

            home_search_box_page.from_input_box().click()
            home_search_box_page.to_input_box().click()
            home_search_box_page.to_search_input_box().send_keys(from_to_search_data["SearchCity"])
            try:
                explicit_wait.until(expected_conditions.visibility_of_element_located(home_search_box_page.TO_DROPDOWN_BOX_LOCATOR))
            except:
                assert int(from_to_search_data["ExpectedLen"]) == 0
                return
            to_cities = home_search_box_page.to_dropdown_items()
            assert len(to_cities) == int(from_to_search_data["ExpectedLen"])
            if len(to_cities) > 0:
                to_city = to_cities[int(from_to_search_data["CityIndexToSelect"])]
                actual_city_name = home_search_box_page.get_city_name(to_city)
                actual_city_desc = home_search_box_page.get_city_description(to_city).replace("-", ",")
                to_city.click()
                expected_to_city_name = home_search_box_page.to_search_input_box().get_attribute("value")
                expected_to_city_desc = home_search_box_page.dest_airport().text
                assert expected_to_city_desc == actual_city_desc
                assert expected_to_city_name in expected_to_city_name
        except:
            logger.exception("")
            assert False

    def test_departure_date(self, logger, home_search_box_page, explicit_wait, date_data):
        try:
            self.driver.refresh()
            date_to_be_selected = datetime.today() + timedelta(days=int(date_data["Date"]))

            try:
                home_search_box_page.set_date(date_to_be_selected, "from")
                set_date = self.driver.find_element_by_id("Fly_depdate").get_attribute("value")
                assert set_date == date_to_be_selected.strftime("%m/%d/%Y")
            except DateNotSelectable:
                if date_to_be_selected.date() < datetime.today().date():
                    set_date = home_search_box_page.depart_date_input_value().get_attribute("value")
                    assert set_date != date_to_be_selected.strftime("%m/%d/%Y")
                else:
                    assert False
        except:
            logger.exception("")
            assert False

    def test_return_date(self, logger, home_search_box_page, explicit_wait, date_data):
        depart_date_to_be_selected = datetime.today() + timedelta(days=int(date_data["Depart"]))
        return_date_to_be_selected = datetime.today() + timedelta(days=int(date_data["Return"]))
        self.driver.refresh()
        try:
            home_search_box_page.set_date(depart_date_to_be_selected, "from")
            set_depart_date = home_search_box_page.depart_date_input_value().get_attribute("value")
            assert set_depart_date == depart_date_to_be_selected.strftime("%m/%d/%Y")

            try:
                home_search_box_page.set_date(return_date_to_be_selected, "to")
                set_return_date = home_search_box_page.return_date_input_value().get_attribute("value")
                assert set_return_date == return_date_to_be_selected.strftime("%m/%d/%Y")
            except DateNotSelectable:
                if return_date_to_be_selected.date() < depart_date_to_be_selected.date():
                    assert True
                else:
                    assert False
        except:
            logger.exception("")
            assert False

    def test_travellers_dropdown_box(self, top_nav, logger, home_search_box_page):
        try:
            home_search_box_page.traveller_details_display().click()
            assert home_search_box_page.travellers_dropdown_box().is_displayed()
        except:
            logger.exception("")
            assert False
        finally:
            top_nav.home_link().click()

    def test_adult_control_buttons(self, logger, top_nav, home_search_box_page, explicit_wait):
        try:
            home_search_box_page.reset_travellers_details()
            number = 12
            for i in range(2, number):
                home_search_box_page.adult_plus_checkbox().click()
                if i == 10:
                    alert = self.driver.switch_to_alert()
                    explicit_wait.until(expected_conditions.alert_is_present())
                    assert "Total no of person should not be more than 9!" in alert.text
                    alert.accept()
                    assert not home_search_box_page.adult_plus_checkbox().is_enabled()
                    assert "9" == home_search_box_page.adult_count_display_box().get_attribute("value")
                else:
                    if i > 9:
                        assert "9" == home_search_box_page.adult_count_display_box().get_attribute("value")
                    else:
                        assert str(i) == home_search_box_page.adult_count_display_box().get_attribute("value")
            for i in range(1, 9):
                home_search_box_page.adult_minus_checkbox().click()
                assert str(9-i) == home_search_box_page.adult_count_display_box().get_attribute("value")
        except:
            logger.exception("")
            assert False
        finally:
            top_nav.home_link().click()

    def test_child_control_button(self, logger, top_nav,  home_search_box_page):
        try:
            home_search_box_page.reset_travellers_details()
            number = 11
            for i in range(1, number):
                home_search_box_page.children_plus_checkbox().click()
                if i == 9:
                    alert = self.driver.switch_to_alert()
                    assert "Total no of person should not be more than 9!" in alert.text
                    alert.accept()
                    assert not home_search_box_page.children_plus_checkbox().is_enabled()
                    assert "8" == home_search_box_page.children_count_display_box().get_attribute("value")
                else:
                    if i > 9:
                        assert "8" == home_search_box_page.children_count_display_box().get_attribute("value")
                    else:
                        assert str(i) == home_search_box_page.children_count_display_box().get_attribute("value")
            for i in range(1, 9):
                home_search_box_page.children_minus_checkbox().click()
                assert str(8-i) == home_search_box_page.children_count_display_box().get_attribute("value")
        except:
            logger.exception('')
            assert False
        finally:
            top_nav.home_link().click()

    def test_infant_control(self, logger, home_search_box_page):
        try:
            home_search_box_page.reset_travellers_details()
            number = 11
            for i in range(1, 9):
                home_search_box_page.infant_plus_checkbox().click()
                if i == 9:
                    alert = self.driver.switch_to_alert()
                    assert "Total no of person should not be more than 9!" in alert.text
                    alert.accept()
                    assert "8"== home_search_box_page.infant_count_display_checkbox().get_attribute("value")
                    assert not home_search_box_page.infant_plus_checkbox().is_displayed()
                else:
                    if i < 9:
                        assert str(i) == home_search_box_page.infant_count_display_checkbox().get_attribute("value")
                    else:
                        assert "8" == home_search_box_page.infant_count_display_checkbox().get_attribute("value")
        except:
            logger.exception("")
            assert False

    def test_choose_travel_class_textbox(self, logger, home_search_box_page, traveller_class_data):
        try:
            self.driver.refresh()
            select = Select(home_search_box_page.travel_class_input_box())
            home_search_box_page.travel_class_display().click()
            home_search_box_page.travel_class_input_box().click()
            select.select_by_index(traveller_class_data["IndexClass"])
            text = select.first_selected_option.text
            home_search_box_page.travel_class_done_button().click()
            assert traveller_class_data["ExpectedClass"] == text
        except:
            logger.exception("")
            assert False

    def set_travellers_data(self, home_search_box_page, adult_count, child_count, infant_count):

        home_search_box_page.reset_travellers_details()
        for i in range(1, adult_count):
            home_search_box_page.adult_plus_checkbox().click()
        for i in range(0, child_count):
            home_search_box_page.children_plus_checkbox().click()
        for i in range(0, infant_count):
            home_search_box_page.infant_plus_checkbox().click()

    def test_travel_class_display_box(self, top_nav, logger, home_search_box_page, traveller_class_data):
        try:
            self.set_travellers_data(home_search_box_page, int(traveller_class_data["AdultCount"]), int(traveller_class_data["ChildCount"]), int(traveller_class_data["InfantCount"]))
            home_search_box_page.travel_class_done_button().click()
            display_count = (home_search_box_page.traveller_details_display().find_element_by_id("travel_id")).text
            assert (display_count) == traveller_class_data["ExpectedTotalTraveller"]
        except:
            logger.exception("")
            assert False
        finally:
            top_nav.home_link().click()

    def test_search_button(self, logger, explicit_wait, home_search_box_page, search_button_data, top_nav):

        try:
            top_nav.home_link().click()
            self.driver.refresh()
            if search_button_data["RoundTrip"] == "Yes":
                home_search_box_page.round_trip_button().click()
            else:
                home_search_box_page.one_way_button().click()
            home_search_box_page.from_input_box().click()
            explicit_wait.until(expected_conditions.visibility_of_element_located(home_search_box_page.FROM_SEARCH_INPUT_BOX_LOCATOR))
            home_search_box_page.from_search_input_box().send_keys(search_button_data["FromText"])
            explicit_wait.until(expected_conditions.visibility_of_element_located(home_search_box_page.FROM_DROPDOWN_BOX_LOCATOR))
            from_city = home_search_box_page.from_dropdown_items()[(int(search_button_data["FromCityIndex"]))].click()
            home_search_box_page.to_input_box().click()
            home_search_box_page.to_search_input_box().send_keys(search_button_data["ToText"])
            explicit_wait.until(expected_conditions.visibility_of_element_located(home_search_box_page.TO_DROPDOWN_BOX_LOCATOR))
            to_city = home_search_box_page.to_dropdown_items()[(int(search_button_data["TocityIndex"]))].click()
            dept_date_to_be_selected = datetime.today() + timedelta(days=int(search_button_data["DeptDate"]))
            home_search_box_page.set_date(dept_date_to_be_selected, "from")
            home_search_box_page.from_input_box().click()
            if search_button_data["RoundTrip"] == "Yes" and search_button_data["RetDate"] != "":
                return_date_to_be_selected = datetime.today() + timedelta(days=int(search_button_data["RetDate"]))
                home_search_box_page.set_date(return_date_to_be_selected, "to")
            self.set_travellers_data(home_search_box_page, int(search_button_data["AdultCount"]), int(search_button_data["ChildCount"]), int(search_button_data["InfantCount"]))
            home_search_box_page.travel_class_done_button().click()
            home_search_box_page.search_button().click()
            if (search_button_data["IsValidData"]) == "FALSE":
                while True:
                    try:
                        alert = self.driver.switch_to_alert()
                        if search_button_data["RetDate"] == "" and search_button_data["RoundTrip"] == "Yes":
                            assert alert.text == " Please enter return date!!"
                        else:
                            assert "Number of infants should be equal " in alert.text or "Departure Airport and Destination Airport can't be same!!" in alert.text
                        alert.accept()
                        break
                    except:
                        logger.debug("Alert not found so waiting")
            else:
                assert self.driver.find_element_by_id("modifysearch").get_attribute("type") == "submit"
        except:
            logger.exception("")
            assert False

    def test_best_offers(self, home_search_box_page, logger, explicit_wait, top_nav):
        try:
            top_best_offers_count = len(home_search_box_page.best_offers())
            for i in range(0, top_best_offers_count):
                link = home_search_box_page.best_offers()[i]
                href = link.find_element_by_xpath("a").get_attribute("href")
                link.click()
                assert href == self.driver.current_url
                top_nav.home_link().click()
        except:
            logger.exception("")
            assert False

    def test_container_new_offers(self, home_search_box_page, logger, top_nav):
        try:
            new_offers = home_search_box_page.container_new_offers()
            for i in range(0, len(new_offers)):
                new_offer = home_search_box_page.container_new_offers()[i]
                href = new_offer.find_element_by_xpath("a").get_attribute("href")
                new_offer.click()
                assert href == self.driver.current_url
                top_nav.home_link().click()
        except:
            logger.exception("")
            assert False

    def test_top_destinations(self, home_search_box_page,logger, top_nav):
        try:
            top_destinations = len(home_search_box_page.top_destinations())
            for i in range(0, top_destinations):
                top_destination = home_search_box_page.top_destinations()[i]
                on_click_text = top_destination.find_element_by_xpath("a").get_attribute("onclick")
                top_destination.click()
                from_dest = self.driver.find_element_by_id("flying_from_old").get_attribute("value")
                to_dest =  self.driver.find_element_by_id("flying_to_old").get_attribute("value")
                assert from_dest in on_click_text
                assert to_dest in on_click_text
                top_nav.home_link().click()
        except:
            logger.exception("")
            assert False

    def test_top_routes(self, top_nav, logger, home_search_box_page, explicit_wait):
        try:
            top_routes = home_search_box_page.top_routes()
            for i in range(0, len(top_routes)):
                top_rout = home_search_box_page.top_routes()[i]
                href = top_rout.get_attribute("href")
                top_rout.click()
                assert href == self.driver.current_url
                top_nav.home_link().click()
        except:
            logger.exception("")
            assert False





















































































