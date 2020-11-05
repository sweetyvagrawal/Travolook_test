import csv

import pytest

from Utilities.utility import get_test_data_path


def load_emails_data():
    with open(get_test_data_path() + "Login/Email_TestData.csv") as emails:
        return list(csv.DictReader(emails))


@pytest.fixture(params=load_emails_data())
def email_data(request):
    return request.param


def load_mobile_data():
    with open(get_test_data_path() + "ContactUs/mobile_data.csv") as mobile_data:
        return list(csv.DictReader(mobile_data))


@pytest.fixture(params=load_mobile_data())
def mobile_data(request):
    return request.param
