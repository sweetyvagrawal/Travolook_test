import csv
import pytest
from selenium.webdriver.support import expected_conditions
from Utilities.EmailData_ import email_data
from Utilities.utility import get_test_data_path


def load_create_account_data():
    with open(get_test_data_path() + "CreateAccount/create_account_test_data.csv") as c_account_daa:
        return list(csv.DictReader(c_account_daa))


@pytest.fixture(params=load_create_account_data())
def create_account_data(request):
    return request.param


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("logger")
@pytest.mark.usefixtures("explicit_wait")
@pytest.mark.usefixtures("create_account_page")
@pytest.mark.usefixtures("top_nav")
@pytest.mark.usefixtures("login_page")
class TestCreateAccount:
    def test_create_account_window_labels(self, logger, create_account_page, top_nav, login_page):
        try:
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            assert create_account_page.first_name_label().text == "First Name"
            assert create_account_page.last_name_label().text == "Last Name"
            assert create_account_page.email_label().text == "Email"
            assert create_account_page.password_label().text == "Password"
            assert create_account_page.create_account_button().get_attribute("value") == "Create an Account"
            assert create_account_page.already_register_link().get_attribute("value") == "Already Registered? Login"
        except:
            logger.exception("")
            assert False
        finally:
            create_account_page.already_register_link().click()
            login_page.close_button().click()

    def test_special_characters_first_last_name(self, create_account_page, logger, top_nav, login_page):
        try:
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            create_account_page.first_name_input_box().send_keys("&*()1234")
            create_account_page.last_name_input_box().send_keys("&*()1234")
            assert create_account_page.last_name_input_box().get_attribute("value") == ""
            assert create_account_page.first_name_input_box().get_attribute("value") == ""
        except:
            logger.exception("")
            assert False
        finally:
            create_account_page.already_register_link().click()
            login_page.close_button().click()

    def test_empty_value_in_create_account_window_input_boxes(self, logger, create_account_page, top_nav, login_page):
        try:
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            create_account_page.first_name_input_box().clear()
            create_account_page.last_name_input_box().clear()
            create_account_page.first_name_input_box().send_keys("")
            create_account_page.last_name_input_box().send_keys("")
            create_account_page.email_input_box().send_keys("")
            create_account_page.password_input_box().send_keys("")
            assert create_account_page.first_name_input_box().get_attribute("value") == ""
            assert create_account_page.last_name_input_box().get_attribute("value") == ""
            assert create_account_page.email_input_box().get_attribute("value") == ""
            assert create_account_page.password_input_box().get_attribute("value") == ""
        except:
            logger.exception("")
            assert False
        finally:
            create_account_page.already_register_link().click()
            login_page.close_button().click()

    def test_email_input_box(self, logger, create_account_page, top_nav, login_page, email_data):
        try:
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            create_account_page.email_input_box().clear()
            create_account_page.email_input_box().send_keys(email_data["Email_Id"])
            create_account_page.create_account_button().click()
            if email_data["Email_Validity"] == "TRUE":
                assert not create_account_page.email_container().is_displayed()
            else:
                create_account_page.email_container().is_displayed()
                if email_data["Email_Id"] == "":
                    assert create_account_page.email_container().text == "Please Enter Email Address"
                else:
                    assert create_account_page.email_container().text == "Please Enter Valid Email"
        except:
            logger.exception("error occured. Data:" + email_data["Email_Id"] + ". Email_Validity: " + email_data["Email_Validity"])
            assert False
        finally:
            create_account_page.already_register_link().click()
            login_page.close_button().click()

    def test_create_account_link(self, logger, top_nav, login_page, create_account_page, explicit_wait, create_account_data):
        try:
            self.driver.refresh()
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            create_account_page.first_name_input_box().send_keys(create_account_data["FirstName"])
            create_account_page.last_name_input_box().send_keys(create_account_data["LastName"])
            create_account_page.email_input_box().send_keys(create_account_data["Email_Id"])
            create_account_page.password_input_box().send_keys(create_account_data["Password"])
            create_account_page.create_account_button().click()
            if create_account_data["Data_Complete"] == "FALSE":
                try:
                    alert = self.driver.switch_to.alert
                    assert alert.text == "Please Select Terms & Conditions"
                    alert.accept()

                except:
                    assert create_account_page.window().is_displayed()

            else:
                explicit_wait.until(expected_conditions.alert_is_present())
                alert = self.driver.switch_to.alert
                if create_account_data["Is_Registered"] == "No":
                    assert alert.text == "You have successfully registered with us."
                    alert.accept()
                    top_nav.my_account_link().click()
                    top_nav.sign_out_dropdown_item().click()
                else:
                    assert alert.text == "You are already registered."
                    alert.accept()
        except:
            logger.exception("")
            assert False
        finally:
            try:
                if create_account_data["Is_Registered"] != "No":
                    create_account_page.close_button().click()
            except:
                logger.exception("")

    def test_already_registered_link(self, top_nav, login_page, logger, create_account_page):
        try:
            top_nav.login_link().click()
            login_page.create_an_account_link().click()
            create_account_page.already_register_link().click()
            assert login_page.login_window().is_displayed()
        except:
            logger.exception("")
            assert False





















