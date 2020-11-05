import inspect
import logging

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from POM.ContactUs import ContactUs
from POM.CreateAnAccountPage import CreateAnAccountPage
from POM.FooterNav import FooterNav
from POM.ForgetPasswordPage import ForgotPasswordPage
from POM.LoginPage import LoginPage
from POM.TopNav import TopNav


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.travolook.in/")
    request.cls.driver = driver
    driver.implicitly_wait(5)

    yield
    driver.quit()


@pytest.fixture(scope="function")
def explicit_wait(request) -> WebDriverWait:
    return WebDriverWait(request.cls.driver, 30)


@pytest.fixture(scope="function")
def action_chains(request) -> ActionChains:
    return ActionChains(request.cls.driver)


@pytest.fixture(scope="function")
def logger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    file_handler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)
    return logger


@pytest.fixture(scope="function")
def top_nav(request) -> TopNav:
    return TopNav(request.cls.driver)


@pytest.fixture(scope="function")
def footer_nav(request) -> FooterNav:
    return FooterNav(request.cls.driver)


@pytest.fixture(scope="function")
def login_page(request) -> LoginPage:
    return LoginPage(request.cls.driver)


@pytest.fixture(scope="function")
def forgot_password_page(request) -> ForgotPasswordPage:
    return ForgotPasswordPage(request.cls.driver)


@pytest.fixture(scope="function")
def create_account_page(request) -> CreateAnAccountPage:
    return CreateAnAccountPage(request.cls.driver)


@pytest.fixture(scope="function")
def contact_us_page(request) -> ContactUs:
    return ContactUs(request.cls.driver)
