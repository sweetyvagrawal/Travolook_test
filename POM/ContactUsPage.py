from selenium import webdriver


class ContactUsPage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def full_name_input_box(self):
        return self.driver.find_element_by_xpath("//div/input[@id='txtFName']")

    def email_input_box(self):
        return self.driver.find_element_by_xpath("//div/input[@id='txtEmail']")

    def mobile_number_input_box(self):
        return self.driver.find_element_by_xpath("//div/input[@id='txtPhone']")

    def message_input_box(self):
        return self.driver.find_element_by_xpath("//div/textarea[@id='MsgTextBox']")

    def send_now_button(self):
        return self.driver.find_element_by_xpath("//div/input[@value='Send Now']")
