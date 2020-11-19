import csv
import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions

import POM
from POM.TopNav import TopNav
from Utilities.utility import get_test_data_path


def load_iteration_data():
    with open(get_test_data_path() + "TopNav/TopNav_Iteration_TestData.csv") as iteration_file:
        return iteration_file.readlines()


def load_links_data():
    with open(get_test_data_path() + "TopNav/TopNav_Links_TestData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


def load_contact_us_data():
    with open(get_test_data_path() + "TopNav/TopNav_ContactUs_TestData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_contact_us_data(), scope="class")
def contact_us_data(request):
    return request.param


@pytest.fixture(params=load_iteration_data(), scope="class")
def url(request):
    return request.param


@pytest.fixture(params=load_links_data(), scope="class")
def link(request):
    return request.param


@pytest.mark.usefixtures("setup")
class TestTopNav:

    def test_brand_link(self, logger, top_nav: POM.TopNav, url):
        try:
            self.driver.get(url)
            top_nav.brand_link().click()
            content_text = self.driver.find_element_by_xpath("//div[@class='searchEng']/h3").text
            assert content_text == "Book Domestic and International flights"
            assert self.driver.current_url == "https://www.travolook.in/"
            assert self.driver.title == "Book Flights Tickets for Domestic & International Destinations"
        except:
            logger.exception("")
            assert False

    def test_brand_image(self, logger, top_nav: TopNav):
        try:
            src = top_nav.brand_image().get_attribute("src")
            assert src == "https://www.travolook.in/images/svg/svg-logo.svg"
        except:
            logger.exception("")
            assert False

    def test_all_header_links(self, url, logger, explicit_wait, link):
        try:
            self.driver.get(url)
            self.driver.find_element_by_xpath(link["Target_Element"]).click()
            text = self.driver.find_element_by_xpath(link["Target_Element"]).text
            content_text = self.driver.find_element_by_xpath(link["Target_Element_To_Test"]).text


            assert content_text == link["Expected_Element_Text"]
            assert text == link["Expected_Link_Text"]
            assert self.driver.current_url == link["Expected_Url"]
            assert self.driver.title == link["Expected_Title"]
        except:
            logger.exception("")
            assert False

    def test_contact_us_link(self, top_nav: TopNav, action_chains: ActionChains, explicit_wait, logger, url):
        try:
            self.driver.get(url)
            contact_us_link = top_nav.contact_us_link()
            text = contact_us_link.text
            action_chains.move_to_element(top_nav.contact_us_link()).perform()
            explicit_wait.until(expected_conditions.visibility_of_element_located(top_nav.CONTACT_US_DROPDOWN_MENU))
            assert text == "24x7Support"
            assert "background-color: rgb(73, 81, 103); display: block;" == top_nav.contact_us_dropdown_menu().get_attribute("style")
            dropdown_items_list = top_nav.contact_us_dropdown_items()
            assert len(dropdown_items_list) == 6 or len(dropdown_items_list) == 2
        except:
            logger.exception("")
            assert False

    def test_contact_us_dropdown_items(self, top_nav: TopNav, action_chains: ActionChains, contact_us_data, url, logger):

        try:
            self.driver.get(url)
            contact_us_link = top_nav.contact_us_link()
            action_chains.move_to_element(top_nav.contact_us_link).perform()
            text = self.driver.find_element_by_xpath(contact_us_data["Dropdown_Menu_Item_Element"]).text + "1"
            self.driver.find_element_by_xpath(contact_us_data["Dropdown_Menu_Item_Element"]).click()
            content_text = self.driver.find_element_by_xpath(contact_us_data["Target_Content_Element"]).text
            assert text == contact_us_data["Expected_dropdown_item_Text"]
            assert content_text == contact_us_data["Expected_Content_Text"]
            assert self.driver.current_url == contact_us_data["Expected_Url"]
            assert self.driver.title == contact_us_data["Expected_Title"]
        except Exception as ex:
            logger.error("Error occurred while running test with url: " + url)

    def test_login_link(self, logger, top_nav: TopNav, url):
        try:
            self.driver.get(url)
            top_nav.login_link().click()
            class_value = top_nav.login_link().get_attribute("class")
            assert class_value == "login login_top login_top_active"
        except:
            logger.exception("")
            assert False






























