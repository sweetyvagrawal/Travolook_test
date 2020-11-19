from selenium import webdriver
from selenium.webdriver.common.by import By


class TopNav:
    LOGIN_LINK_LOCATOR = (By.ID, "login_top1")
    CONTACT_LINK_LOCATOR = (By.XPATH, "//nav/div/div/ul[1]/li[4]/a")
    CONTACT_US_DROPDOWN_MENU = (By.XPATH, "//li[@id='resclick']/div[@class='dropdown-menu']")

    def __init__(self, driver: webdriver):
        self.driver = driver

    def home_link(self):
        return self.driver.find_element_by_xpath("//nav/div/div/ul[1]/li[1]/a")

    def offer_link(self):
        return self.driver.find_element_by_xpath("//nav/div/div/ul[1]/li[2]/a")

    def sitemap_link(self):
        return self.driver.find_element_by_xpath("//nav/div/div/ul[1]/li[3]/a")

    def contact_link(self):
        return self.driver.find_element(self.CONTACT_LINK_LOCATOR[0], self.CONTACT_LINK_LOCATOR[1])

    def make_payment_link(self):
        return self.driver.find_element_by_xpath("//nav/div/div/ul[1]/li[5]/a")

    def brand_link(self):
        return self.driver.find_element_by_xpath("//a[@class='navbar-brand']")

    def brand_image(self):
        return self.driver.find_element_by_xpath("//a[@class='navbar-brand']/img")

    def contact_us_link(self):
        return self.driver.find_element_by_xpath("//li[@id='resclick']/a")

    def contact_us_dropdown_menu(self):
        return self.driver.find_element(self.CONTACT_US_DROPDOWN_MENU[0], self.CONTACT_US_DROPDOWN_MENU[1])

    def contact_us_dropdown_items(self):
        return self.driver.find_elements_by_xpath("//li[@id='resclick']/div[@class='dropdown-menu']/a")

    def contact_us_dropdown_item(self):
        return self.driver.find_element_by_xpath("//li[@id='resclick']/div[@class='dropdown-menu']/a[1]")

    def reschedule_dropdown_item(self):
        return self.driver.find_element_by_xpath("//li[@id='resclick']/div[@class='dropdown-menu']/a[2]")

    def login_link(self):
        return self.driver.find_element(self.LOGIN_LINK_LOCATOR[0], self.LOGIN_LINK_LOCATOR[1])

    def my_account_link(self):
        return self.driver.find_element_by_xpath("//a[@id='myaccount']")

    def sign_out_dropdown_item(self):
        return self.driver.find_element_by_xpath("//a[@onclick='logout()']")


