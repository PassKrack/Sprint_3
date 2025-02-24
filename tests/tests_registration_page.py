from locators import REGISTRATION_BUTTON_LOCATOR, REGISTRATION_FORM_TITLE_LOCATOR, PERSONAL_ACCOUNT_LOCATOR, \
    REGISTRATION_NAME_INPUT_LOCATOR, REGISTRATION_EMAIL_INPUT_LOCATOR, REGISTRATION_PASSWORD_INPUT_LOCATOR, \
    COMPLETE_REGISTRATION_BUTTON, \
    ERROR_TEXT_INPUT_LOCATOR, AUTH_FORM_TITLE_LOCATOR, AUTH_EMAIL_INPUT_LOCATOR, AUTH_PASSWORD_INPUT_LOCATOR, \
    AUTH_BUTTON_LOCATOR, LOGOUT_BUTTON_LOCATOR
from settings import fake
from steps import Steps
import re


class TestStellarBurgersRegistration:

    def test_success_registration_new_user(self, driver):
        email = fake.email()
        login = email.split('@')[0]
        new_user = Steps()
        new_user.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_BUTTON_LOCATOR)
        new_user.wait_element(driver, REGISTRATION_FORM_TITLE_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        new_user.input_user_name(driver, REGISTRATION_NAME_INPUT_LOCATOR, login)
        name_value = new_user.get_field_value(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        assert name_value
        new_user.click_to_element(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        new_user.input_user_email(driver, REGISTRATION_EMAIL_INPUT_LOCATOR, email)
        email_value = new_user.get_field_value(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        assert re.fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", email_value)
        new_user.click_to_element(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        password = fake.password(6)
        new_user.input_user_password(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR, password)
        password_value = new_user.get_field_value(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        assert len(password_value) >= 6
        new_user.click_to_element(driver, COMPLETE_REGISTRATION_BUTTON)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
        Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, email)
        Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
        Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, password)
        Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        quit_button = Steps.find_element(driver, LOGOUT_BUTTON_LOCATOR)
        assert quit_button

    def test_failed_incorrect_password_validation(self, driver):
        new_user = Steps()
        new_user.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_BUTTON_LOCATOR)
        new_user.wait_element(driver, REGISTRATION_FORM_TITLE_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        new_user.input_user_name(driver, REGISTRATION_NAME_INPUT_LOCATOR, fake.email().split('@'))
        new_user.click_to_element(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        new_user.input_user_email(driver, REGISTRATION_EMAIL_INPUT_LOCATOR, 'BurgerD')
        new_user.click_to_element(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        new_user.input_user_password(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR, '1234q')
        new_user.click_to_element(driver, COMPLETE_REGISTRATION_BUTTON)
        error_message = new_user.find_element(driver, ERROR_TEXT_INPUT_LOCATOR)
        assert error_message is not None