from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    def login_window(self):
        return self.driver.find_element_by_id("login_top_open1")

    def close_button(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/i[@class='closelogin']")

    def email_label(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/label[1]")

    def email_input(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/input[@id='txtloginemail']")

    def invalid_email_label(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/div[@id='phn1']/ul/li")

    def invalid_email_container(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/div[@id='phn1']")

    def password_label(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/label[2]")

    def invalid_password_label(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/div[@id='pass1']/ul/li")

    def invalid_password_container(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/div[@id='pass1']")

    def password_input(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/input[@id='txtloginpassword']")

    def remember_me_checkbox(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/input[@id='chkrember']")

    def remember_me_label(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/label[3]")

    def forgot_password_link(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/a[1]")

    def sign_in_button(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/input[@value='Sign In']")

    def create_an_account_link(self):
        return self.driver.find_element_by_xpath("//div[@id='login']/a[2]")









