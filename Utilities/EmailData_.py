import csv

import pytest

from Utilities.utility import get_test_data_path


def load_emails_data():
    with open(get_test_data_path() + "Login/Email_TestData.csv") as emails:
        return list(csv.DictReader(emails))


@pytest.fixture(params=load_emails_data())
def email_data(request):
    return request.param
