import pytest
from selenium.webdriver.support import expected_conditions
from Utilities.data_fixtures import email_data, mobile_data, contact_us_link_data, message_data


@pytest.fixture(params=[{"name": "", "is_valid": False}, {"name": "tom", "is_valid": True}], scope="class")
def name_input_data(request):
    return request.param


@pytest.mark.usefixtures("setup")
class TestContactUs:

    def test_empty_input_boxes(self, logger, top_nav, contact_us_page):
        try:
            top_nav.contact_link().click()
            contact_us_page.full_name_input_box().send_keys("")
            contact_us_page.email_input_box().send_keys("")
            contact_us_page.mobile_number_input_box().send_keys("")
            contact_us_page.message_input_box().send_keys("")
            contact_us_page.send_now_button().click()
            alert = self.driver.switch_to.alert
            assert alert.text == "Please enter your Name"
            alert.accept()
            assert contact_us_page.full_name_input_box().get_attribute("value") == ""
            assert contact_us_page.mobile_number_input_box().get_attribute("value") == ""
            assert contact_us_page.email_input_box().get_attribute("value") == ""
            assert contact_us_page.message_input_box().get_attribute("value") == ""
        except:
            logger.exception("")
            assert False

    def test_full_name_input_box(self, logger, explicit_wait, top_nav, contact_us_page, name_input_data):
        try:
            top_nav.contact_link().click()
            contact_us_page.full_name_input_box().send_keys(name_input_data["name"])
            contact_us_page.email_input_box().send_keys("abc@abc.com")
            contact_us_page.mobile_number_input_box().send_keys("1234567891")
            contact_us_page.message_input_box().send_keys("hi")
            contact_us_page.send_now_button().click()
            explicit_wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            if not name_input_data["is_valid"]:
                assert alert.text == "Please enter your Name"
            else:
                assert alert.text == "Your request has been successfully submitted."
            alert.accept()
        except:
            logger.exception("")
            assert False

    def test_email_input_box(self, logger, top_nav, explicit_wait, contact_us_page, email_data):
        try:
            explicit_wait.until(expected_conditions.element_to_be_clickable(top_nav.CONTACT_LINK_LOCATOR))
            top_nav.contact_link().click()
            contact_us_page.full_name_input_box().send_keys("Tom")
            contact_us_page.email_input_box().send_keys(email_data["Email_Id"])
            contact_us_page.mobile_number_input_box().send_keys("7777777777")
            contact_us_page.message_input_box().send_keys("hi")
            contact_us_page.send_now_button().click()
            explicit_wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            if email_data["Email_Validity"] == "TRUE":
                assert alert.text == "Your request has been successfully submitted."
            else:
                assert alert.text == "Please enter a valid email address."
            alert.accept()
        except:
            logger.exception("")
            assert False

    def test_mobile_input_box(self, logger, top_nav, explicit_wait, contact_us_page, mobile_data):
        try:
            top_nav.contact_link().click()
            contact_us_page.full_name_input_box().send_keys("Tom")
            contact_us_page.email_input_box().send_keys("abc@abc.com")
            contact_us_page.mobile_number_input_box().clear()
            contact_us_page.mobile_number_input_box().send_keys(mobile_data["Number"])
            contact_us_page.message_input_box().send_keys("hi")
            contact_us_page.send_now_button().click()
            explicit_wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            if mobile_data["Is_Valid"] == "No":
                assert alert.text == "Please enter a valid phone number."
            else:
                assert alert.text == "Your request has been successfully submitted."
            alert.accept()
        except:
            logger.exception("")
            assert False

    def test_more_than_10_numbers_in_mobile_input_box(self, top_nav, contact_us_page, logger):

        try:
            top_nav.contact_link().click()
            contact_us_page.mobile_number_input_box().send_keys(123456789123456)
            inbox_value = contact_us_page.mobile_number_input_box().get_attribute("value")
            assert inbox_value == "1234567891"
            assert len(inbox_value) == 10
        except:
            logger.exception("")
            assert False

    def test_send_now_button(self, logger, top_nav,explicit_wait, contact_us_link_data, contact_us_page):
        try:
            explicit_wait.until(expected_conditions.element_to_be_clickable(top_nav.CONTACT_LINK_LOCATOR))
            top_nav.contact_link().click()
            contact_us_page.full_name_input_box().send_keys(contact_us_link_data["Name"])
            contact_us_page.email_input_box().send_keys(contact_us_link_data["Email"])
            contact_us_page.mobile_number_input_box().send_keys(contact_us_link_data["MobileNo"])
            contact_us_page.message_input_box().send_keys(contact_us_link_data["Message"])
            contact_us_page.send_now_button().click()
            explicit_wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            if contact_us_link_data["CompleteData"] == "Yes":
                assert alert.text == "Your request has been successfully submitted."
            else:
                assert alert.text != "Your request has been successfully submitted."
            alert.accept()
            contact_us_page.full_name_input_box().clear()
            contact_us_page.email_input_box().clear()
            contact_us_page.mobile_number_input_box().clear()
            contact_us_page.message_input_box().clear()
        except:
            logger.exception("")
            assert False

    def test_message_input_box(self, logger, contact_us_page, top_nav, explicit_wait, message_data):
        try:
            explicit_wait.until(expected_conditions.element_to_be_clickable(top_nav.CONTACT_LINK_LOCATOR))
            top_nav.contact_link().click()
            contact_us_page.message_input_box().send_keys(message_data["ActualData"])
            value = contact_us_page.message_input_box().get_attribute("value")
            assert value == message_data["ExpectedData"]
        except:
            logger.exception("")
            assert False



























