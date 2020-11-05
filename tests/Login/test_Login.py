import csv
import pytest
from selenium.webdriver.support import expected_conditions

from Utilities.data_fixtures import load_emails_data
from Utilities.utility import get_test_data_path


def load_sign_in_data():
    with open(get_test_data_path() + "Login/SignIn_TestData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))





@pytest.fixture(params=[{"key": "", "IsValid": False}, {"key": "dfasfdsfdsf232", "IsValid": True}])
def password_data(request):
    return request.param


@pytest.fixture(params=load_sign_in_data())
def sign_in_data(request):
    return request.param


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("top_nav")
@pytest.mark.usefixtures("login_page")
@pytest.mark.usefixtures("explicit_wait")
@pytest.mark.usefixtures("logger")
class TestLogin:
    def test_validate_all_labels(self, top_nav, login_page, logger):
        try:
            top_nav.login_link().click()
            assert login_page.email_label().text == "Email"
            assert login_page.close_button().text == "Close"
            assert login_page.email_input().get_attribute("placeholder") == "Enter Email"
            assert login_page.password_label().text == "Password"
            assert login_page.password_input().get_attribute("placeholder") == "Enter Password"
            assert login_page.forgot_password_link().text == "Forgot Password?"
            assert login_page.remember_me_label().text == "Remember me"
            assert login_page.sign_in_button().get_attribute("value") == "Sign In"
            assert login_page.create_an_account_link().text == "New User? Create an Account"
        except:
            logger.warn("", exc_info=True)
            assert False
        finally:
            login_page.close_button().click()

    def test_close_link(self, top_nav, login_page, explicit_wait, logger):
        try:
            top_nav.login_link().click()
            login_page.close_button().click()
            explicit_wait.until(expected_conditions.invisibility_of_element_located(login_page.login_window()))
            assert login_page.login_window().get_attribute("style") == "display: none;"
        except:
            logger.exception("")
            assert False

    def test_forgot_password_link(self, top_nav, login_page, explicit_wait, forgot_password_page, logger):
        try:
            top_nav.login_link().click()
            login_page.forgot_password_link().click()
            explicit_wait.until(expected_conditions.visibility_of_element_located(forgot_password_page.FORGOT_PASSWORD_WINDOW_LOCATOR))
            assert forgot_password_page.window().get_attribute("style") == "display: block;"
        except:
            logger.exception("")
            assert False
        finally:
            forgot_password_page.back_button().click()
            login_page.close_button().click()

    def test_email_input_box(self, login_page, email_data, logger, top_nav):
        try:
            top_nav.login_link().click()
            login_page.email_input().send_keys(email_data["Email_Id"])
            login_page.sign_in_button().click()
            if email_data["Email_Validity"] == "TRUE":
                assert not login_page.invalid_email_container().is_displayed()
            else:
                assert login_page.invalid_email_container().is_displayed()
                if email_data["Email_Id"] == "":
                    assert login_page.invalid_email_label().text == "Enter Email Address"
                else:
                    assert login_page.invalid_email_label().text == "Enter Valid Email"
            login_page.email_input().clear()
        except:
            logger.error("", exc_info=True)
            assert False
        finally:
            login_page.close_button().click()

    def test_password_input_box(self, top_nav, login_page, logger, password_data):
        try:
            top_nav.login_link().click()
            login_page.email_input().send_keys("ddasfdsfdfd@vdfa.com")
            login_page.password_input().send_keys(password_data["key"])
            login_page.sign_in_button().click()
            if not password_data["IsValid"]:
                assert login_page.invalid_password_container().is_displayed()
                assert login_page.invalid_password_label().text == "Please Enter Password"
            else:
                assert not login_page.invalid_password_container().is_displayed()
        except:
            logger.exception("")
            assert False
        finally:
            login_page.close_button().click()

    def test_sign_in_button(self, top_nav, login_page, logger, sign_in_data, explicit_wait):
        try:
            explicit_wait.until(expected_conditions.presence_of_element_located(top_nav.LOGIN_LINK_LOCATOR))
            top_nav.login_link().click()
            login_page.email_input().clear()
            login_page.password_input().clear()
            login_page.email_input().send_keys(sign_in_data["EmailID"])
            login_page.password_input().send_keys(sign_in_data["Password"])
            login_page.sign_in_button().click()

            if sign_in_data["IsRegistered"] == "TRUE":
                assert top_nav.my_account_link().text == "My Account"
                top_nav.my_account_link().click()
                top_nav.sign_out_dropdown_item().click()

            else:
                explicit_wait.until(expected_conditions.alert_is_present())
                alert = self.driver.switch_to.alert
                assert alert.text == "Your UserID or Password does not match. Please try again!"
                alert.accept()
                login_page.close_button().click()
        except:
            logger.exception("")
            assert False












































































