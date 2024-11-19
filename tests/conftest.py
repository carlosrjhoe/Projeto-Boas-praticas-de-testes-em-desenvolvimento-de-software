import pytest
from selenium.webdriver import Chrome


@pytest.fixture
def webdriver():
    driver = Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()
