import pytest
from selenium.webdriver.support import expected_conditions
from Utilities.data_fixtures import email_data
from tests.conftest import action_chains


@pytest.mark.usefixtures("setup")
class TestForgotPassWord:
    def test_validate_forgot_password_window_label(self, logger, forgot_password_page, top_nav, login_page):
        try:
            top_nav.login_link().click()
            login_page.forgot_password_link().click()
            assert forgot_password_page.email_label().text == "Email"
            assert forgot_password_page.submit_button().text == "Submit"
            assert forgot_password_page.back_button().text == "Back"
        except:
            logger.exception("")
        finally:
            forgot_password_page.back_button().click()
            login_page.close_button().click()

    def test_forgot_password_link(self, top_nav, logger, login_page, forgot_password_page, explicit_wait, email_data):
        try:
            self.driver.refresh()
            top_nav.login_link().click()
            login_page.forgot_password_link().click()
            forgot_password_page.email_input_box().send_keys(email_data["Email_Id"])
            forgot_password_page.submit_button().click()
            if email_data["Email_Validity"] == "TRUE":
                explicit_wait.until(expected_conditions.alert_is_present())
                alert = self.driver.switch_to.alert
                try:
                    if email_data["IsRegistered"] == "No":
                        assert alert.text == "You are not authorized user."
                    else:
                        assert alert.text == "Your password  has been sent  to your email address .Please check your mailbox and proceed accordingly."
                finally:
                    alert.accept()
            else:
                try:
                    if email_data["Email_Id"] == "":
                        assert forgot_password_page.email_invalid_container().text == "Please Enter Email Address"
                    else:
                        assert forgot_password_page.email_invalid_container().text == "Please Enter Valid Email"
                finally:
                    forgot_password_page.back_button().click()
                    login_page.close_button().click()
        except:
            logger.exception("")
            assert False

    def test_back_button(self, forgot_password_page, top_nav, logger, login_page, action_chains):
        try:
            top_nav.login_link().click()
            login_page.forgot_password_link().click()
            forgot_password_page.back_button().click()
            assert login_page.login_window().is_displayed()
        except:
            logger.exception("")
            assert False






