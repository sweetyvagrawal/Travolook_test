import csv
import pytest
from selenium.common.exceptions import NoSuchElementException

from Utilities.utility import get_test_data_path


def load_url():
    with open(get_test_data_path() + "FooterNav/FooterNav_url_TestData.csv") as iteration_file:
        return iteration_file.readlines()


def load_link_data():
    with open(get_test_data_path() + "FooterNav/FooterNav_SocialLink_TestData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


def load_footer_link_data():
    with open(get_test_data_path() + "FooterNav/FooterNav_Link_TestData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_footer_link_data(), scope="class")
def footer_link_data(request):
    return request.param


@pytest.fixture(params=load_link_data(), scope="class")
def link(request):
    return request.param


@pytest.fixture(params=load_url(), scope="class")
def url(request):
    return request.param


@pytest.mark.usefixtures("setup")
class TestFooterNav:

    def test_footer_links(self, footer_link_data, url, logger):
        try:
            self.driver.get(url)
            text = self.driver.find_element_by_xpath(footer_link_data["Target_Link"]).text
            self.driver.find_element_by_xpath(footer_link_data["Target_Link"]).click()
            content_text = self.driver.find_element_by_xpath(footer_link_data["Target_Element_Text"]).text
            assert content_text == footer_link_data["Expected_Element_Text"]
            assert text == footer_link_data["Target_Link_Expected_Text"]
            assert self.driver.current_url == footer_link_data["Expected_Url"]
            assert self.driver.title == footer_link_data["Expected_Title"]
        except NoSuchElementException as ex:
            logger.critical("one or more footer links element not found on url: " + url + ". Message: " + ex.msg)
            assert False

    def test_connect_with_us(self, link, url, logger):
        try:
            self.driver.get(url)
            link_element = self.driver.find_element_by_xpath(link["Target_Link"])
            icon_class = link_element.find_element_by_xpath("i").get_attribute("class")
            link_element.click()
            child_wind = self.driver.window_handles[1]
            self.driver.switch_to.window(child_wind)
            assert link["Expected_url"] == self.driver.current_url
            assert link["Expected_Title"] in self.driver.title
            assert link["Icon_Class"] == icon_class
        except NoSuchElementException as ex:
            logger.critical("one or more footer links element not found on url: " + url, exc_info=True)
            assert False
        finally:
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])
