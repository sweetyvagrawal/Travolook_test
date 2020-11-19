import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def initial_setup(request):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://www.amazon.com/")
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield
    driver.quit()

@pytest.mark.usefixtures("initial_setup")
class TestAmazonSearch:
    def test_search(self, explicit_wait, logger):
        assert "https://www.amazon.com/" == self.driver.current_url
        self.driver.find_element_by_id("")









