import time
from datetime import datetime


from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

class DateNotSelectable(Exception):
    pass

class HomeSearchBoxPage:
    FROM_INPUT_BOX_LOCATOR = (By.XPATH, "//input[@id='flying_from_N']")
    TO_INPUT_BOX_LOCATOR = (By.XPATH, "//input[@id='flying_to_N']")
    FROM_SEARCH_INPUT_BOX_LOCATOR = (By.XPATH, "//input[@id='flying_from']")
    TO_SEARCH_INPUT_BOX_LOCATOR = (By.XPATH, "//input[@id='flying_to']")
    FROM_DROPDOWN_BOX_LOCATOR = (By.XPATH, "//body/div[@class='ac_results'][1]")
    TO_DROPDOWN_BOX_LOCATOR = (By.XPATH, "//body/div[@class='ac_results'][2]")
    DATEPICKER_DROPDOWN_LOCATOR = (By.ID, "ui-datepicker-div")
    RETURN_INPUT_BOX_LOCATOR = (By.ID, "Fly_retdate")

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.from_input_box().click()
        self.to_input_box().click()

    def one_way_button(self):
        return self.driver.find_element_by_xpath("//button[@onclick=\"return SelectTripType('O')\"]")

    def round_trip_button(self):
        return self.driver.find_element_by_xpath("//button[@onclick=\"return SelectTripType('R')\"]")

    def from_label(self):
        return self.driver.find_element_by_xpath("//strong[@class='swap']")

    def from_input_box(self):
        return self.driver.find_element(self.FROM_INPUT_BOX_LOCATOR[0], self.FROM_INPUT_BOX_LOCATOR[1])

    def to_input_box(self):
        return self.driver.find_element(self.TO_INPUT_BOX_LOCATOR[0], self.TO_INPUT_BOX_LOCATOR[1])

    def from_search_input_box(self):
        return self.driver.find_element(self.FROM_SEARCH_INPUT_BOX_LOCATOR[0], self.FROM_SEARCH_INPUT_BOX_LOCATOR[1])

    def to_search_input_box(self):
        return self.driver.find_element(self.TO_SEARCH_INPUT_BOX_LOCATOR[0], self.TO_SEARCH_INPUT_BOX_LOCATOR[1])

    def search_button(self):
        return self.driver.find_element_by_xpath("//input[@id='searchengine_btn']")

# TRAVELLERS & CLASS

    def traveller_details_display(self):
        return self.driver.find_element_by_xpath("//div[@id='adult_div']/span")

    def travellers_dropdown_box(self):
        return self.driver.find_element_by_xpath("//div[@class='popup adultdrop']")

    def adult_minus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub1minus']")

    def adult_plus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub1plus']")

    def adult_count_display_box(self):
        return self.driver.find_element_by_xpath("//input[@id='sub1']")

    def children_minus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub2minus']")

    def children_plus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub2plus']")

    def children_count_display_box(self):
        return self.driver.find_element_by_xpath("//input[@id='sub2']")

    def infant_minus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub3minus']")

    def infant_plus_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub3plus']")

    def infant_count_display_checkbox(self):
        return self.driver.find_element_by_xpath("//input[@id='sub3']")

    def travel_class_display(self):
        return self.driver.find_element_by_xpath("//b[@id='cabin_id']")

    def travel_class_input_box(self):
        return self.driver.find_element_by_id("ddlCabinClass")

    def travel_class_done_button(self):
        return self.driver.find_element_by_xpath("//span[@class='done']/a")

# DEPARTURE AND RETURN FUNCTIONALITY

    def from_dropdown_item_box(self):
        return self.driver.find_element(self.FROM_DROPDOWN_BOX_LOCATOR[0], self.FROM_DROPDOWN_BOX_LOCATOR[1])

    def from_dropdown_items(self):
        return self.from_dropdown_item_box().find_elements_by_xpath("ul/li")

    def to_dropdown_item_box(self):
        return self.driver.find_element(self.TO_DROPDOWN_BOX_LOCATOR[0], self.TO_DROPDOWN_BOX_LOCATOR[1])

    def to_dropdown_items(self):
        return self.to_dropdown_item_box().find_elements_by_xpath("ul/li")

    def swap_button(self):
        return self.driver.find_element_by_xpath("//div/img[@title='Swap']")

    def get_city_name(self, city: webelement):
        return city.find_element_by_xpath("b").text

    def get_city_description(self, city: webelement):
        return city.find_element_by_xpath("span").text

    def depart_airport(self):
        return self.driver.find_element_by_id("Fly_Depart_airport")

    def dest_airport(self):
        return self.driver.find_element_by_id("Fly_Dest_airport")

    def date_picker_dropdown_box(self):
        return self.driver.find_element(self.DATEPICKER_DROPDOWN_LOCATOR[0], self.DATEPICKER_DROPDOWN_LOCATOR[1])

    def depart_date_container(self):
        return self.driver.find_element_by_xpath("//div[@id ='Fly_dep_datepickerid']")

    def return_date_container(self):
        return self.driver.find_element_by_xpath("//div[@id ='Fly_ret_datepickerid']")

    def left_days_of_week(self):
        return self.driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']/table/thead/tr/th")

    def right_days_of_week(self):
        return self.driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-last']/table/thead/tr/th")

    def left_month_year_label(self):
        return self.driver.find_element_by_xpath("//div[@class='ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-left']/div")

    def left_year_label(self):
        return self.left_month_year_label().find_element_by_class_name("ui-datepicker-year")

    def left_month_label(self):
        return self.left_month_year_label().find_element_by_class_name("ui-datepicker-month")


    def right_month_year_label(self):
        return self.driver.find_element_by_xpath("//div[@class='ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-right']/div")

    def left_month_dates(self):
        return self.driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-first']/table/tbody/tr/td")

    def right_month_dates(self):
        return self.driver.find_elements_by_xpath("//div[@class='ui-datepicker-group ui-datepicker-group-last']/table/tbody/tr/td")

    def previous_month_scroll_arrow(self):
        return self.driver.find_element_by_xpath("//a[@data-handler='prev']")

    def next_month_scroll_arrow(self):
        return self.driver.find_element_by_xpath("//a[@data-handler='next']")

    def depart_day_display(self):
        return self.driver.find_element_by_id("Fly_dep_day")

    def return_day_display(self):
        return self.driver.find_element_by_id("Fly_ret_day")

    def depart_date_month_display(self):
        return self.driver.find_element_by_id("Fly_depdate_val")

    def return_date_month_display(self):
        return self.driver.find_element_by_id("Fly_retdate_val")

    def depart_date_input_value(self):
        return self.driver.find_element_by_id("Fly_depdate")

    def return_date_input_value(self):
        return self.driver.find_element_by_id("Fly_retdate")

    # BEST OFFERS
    def best_offers(self):
        return self.driver.find_elements_by_class_name("offrbox")

    def container_new_offers(self):
        return self.driver.find_elements_by_xpath('//section[@class="container-fluid newoffer"]/div')

    def top_destinations(self):
        return self.driver.find_elements_by_xpath('//div[@class="vac-topdealsbox"]/ul/li')

    def top_routes(self):
        return self.driver.find_elements_by_xpath('//div[@class="container"]/ul/li/a')


    def set_date(self, date_to_be_selected: datetime, target_date_control):
        try:
            day_to_be_selected = date_to_be_selected.day
            year_to_be_selected = date_to_be_selected.year
            month_to_be_selected = date_to_be_selected.month
            month_year_text_to_be_selected = date_to_be_selected.strftime("%B %Y")
            if target_date_control == "from":
                self.depart_date_container().click()
            else:
                self.return_date_container().click()



            while self.left_month_year_label().text != month_year_text_to_be_selected:
                if int(self.left_year_label().text) > year_to_be_selected:
                    self.previous_month_scroll_arrow().click()
                    continue
                if int(self.left_year_label().text) < year_to_be_selected:
                    self.next_month_scroll_arrow().click()
                    continue
                month_text = self.left_month_label().text
                current_calender_month = "01 " + month_text + " 2020"
                current_date = datetime.strptime(current_calender_month, "%d %B %Y")
                if current_date.month > month_to_be_selected:
                    self.previous_month_scroll_arrow().click()
                    continue
                if current_date.month < month_to_be_selected:
                    self.next_month_scroll_arrow().click()
                    continue

            for date in self.left_month_dates():
                if date.text == str(day_to_be_selected):
                    if date.get_attribute("data-event") is None:
                       raise DateNotSelectable("Given date is not selectable.")
                    date.click()
                    date = self.left_month_label()
                    break
        except NoSuchElementException:
            raise DateNotSelectable("Given date is not selectable.")

    def reset_travellers_details(self):

        self.traveller_details_display().click()
        expected_adult_count = self.adult_count_display_box().get_attribute("value")
        expected_child_count = self.children_count_display_box().get_attribute("value")
        expected_infant_count = self.infant_count_display_checkbox().get_attribute("value")
        while expected_adult_count != "1":
            self.adult_minus_checkbox().click()
            expected_adult_count = self.adult_count_display_box().get_attribute("value")
        while expected_child_count != "0":
            self.children_minus_checkbox().click()
            expected_child_count = self.children_count_display_box().get_attribute("value")
        while expected_infant_count != "0":
            self.infant_minus_checkbox().click()
            expected_infant_count = self.infant_count_display_checkbox().get_attribute("value")

























