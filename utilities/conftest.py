import pytest
from selenium import webdriver
from basic_automation.page_objects.login_page import Practice, NavigateMenu


@pytest.fixture()
def setup_browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def practice_page(setup_browser):
    # Fixture to provide an instance of LogIn page for tests
    return Practice(setup_browser)


@pytest.fixture()
def navigate_menu_page(setup_browser):
    return NavigateMenu(setup_browser)