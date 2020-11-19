import csv

import pytest

from Utilities.utility import get_test_data_path


def load_emails_data():
    with open(get_test_data_path() + "Login/Email_TestData.csv") as emails:
        return list(csv.DictReader(emails))


@pytest.fixture(params=load_emails_data(), scope="class")
def email_data(request):
    return request.param


def load_mobile_data():
    with open(get_test_data_path() + "ContactUs/mobile_data.csv") as mobile_data:
        return list(csv.DictReader(mobile_data))


@pytest.fixture(params=load_mobile_data(), scope="class")
def mobile_data(request):
    return request.param


def load_contact_us_link_data():
    with open(get_test_data_path() + "ContactUs/contactus_link_data.csv")as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_contact_us_link_data(), scope="class")
def contact_us_link_data(request):
    return request.param


def load_message_data():
    with open(get_test_data_path() + "ContactUs/message_data.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_message_data(), scope="class")
def message_data(request):
    return request.param


def load_from_to_search_data():
    with open (get_test_data_path() + "HomeSearchBox/FromToSearchData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_from_to_search_data(), scope="class")
def from_to_search_data(request):
    return request.param


def load_test_date():
    with open(get_test_data_path() + "HomeSearchBox/DateData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_test_date())
def date_data(request):
    return request.param


def load_traveller_class_data():
    with open(get_test_data_path() +"HomeSearchBox/TravellerClassData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_traveller_class_data())
def traveller_class_data(request):
    return request.param


def load_search_button_data():
    with open(get_test_data_path() + "HomeSearchBox/SearchButtonData.csv") as iteration_file:
        return list(csv.DictReader(iteration_file))


@pytest.fixture(params=load_search_button_data())
def search_button_data(request):
    return request.param





