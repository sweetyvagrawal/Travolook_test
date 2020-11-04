from selenium import webdriver
from selenium.webdriver.common.by import By


class ForgotPasswordPage:

    FORGOT_PASSWORD_WINDOW_LOCATOR = (By.ID, "forgot")

    def __init__(self, driver: webdriver):
        self.driver = driver

    def window(self):
        return self.driver.find_element(self.FORGOT_PASSWORD_WINDOW_LOCATOR[0], self.FORGOT_PASSWORD_WINDOW_LOCATOR[1])

    def back_button(self):
        return self.driver.find_element_by_xpath("//input[@value='Back']")

    def submit_button(self):
        return self.driver.find_element_by_xpath("//input[@value='Submit']")

    def email_label(self):
        return self.driver.find_element_by_xpath("//div[@id='forgot']/label")

    def email_input_box(self):
        return self.driver.find_element_by_xpath("//div[@id='forgot']/input[@id='txtforgotemail']")

    def email_invalid_container(self):
        return self.driver.find_element_by_xpath("//div[@id='forgot']/div[@id='phnn']/ul/li")

