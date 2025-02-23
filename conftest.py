import pytest
from selenium import webdriver

from locators import GO_TO_AUTH_BUTTON_LOCATOR, AUTH_FORM_TITLE_LOCATOR, AUTH_EMAIL_INPUT_LOCATOR, \
    AUTH_PASSWORD_INPUT_LOCATOR, AUTH_BUTTON_LOCATOR
from steps import Steps


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def login(driver):
    Steps.click_to_element(driver, GO_TO_AUTH_BUTTON_LOCATOR)
    Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
    Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
    Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, 'BurgerD')
    Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
    Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, '1234qweR)')
    Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)