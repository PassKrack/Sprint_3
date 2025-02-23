from locators import REGISTRATION_BUTTON_LOCATOR, REGISTRATION_FORM_TITLE_LOCATOR, PERSONAL_ACCOUNT_LOCATOR, \
    REGISTRATION_NAME_INPUT_LOCATOR, REGISTRATION_EMAIL_INPUT_LOCATOR, REGISTRATION_PASSWORD_INPUT_LOCATOR, COMPLETE_REGISTRATION_BUTTON, \
    ERROR_TEXT_INPUT_LOCATOR
from steps import Steps
import re


class TestStellarBurgers:

    def test_success_registration_new_user(self, driver):
        new_user = Steps()
        new_user.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_BUTTON_LOCATOR)
        new_user.wait_element(driver, REGISTRATION_FORM_TITLE_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        new_user.input_user_name(driver, REGISTRATION_NAME_INPUT_LOCATOR, 'BurgerDestroyer')
        name_value = new_user.get_field_value(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        assert name_value is not None
        new_user.click_to_element(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        new_user.input_user_email(driver, REGISTRATION_EMAIL_INPUT_LOCATOR, 'BurgerD')
        email_value = new_user.get_field_value(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        assert re.fullmatch("([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)", email_value)
        new_user.click_to_element(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        new_user.input_user_password(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR, '1234qweR)')
        password_value = new_user.get_field_value(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        assert len(password_value) >= 6
        new_user.click_to_element(driver, COMPLETE_REGISTRATION_BUTTON)

    def test_failed_incorrect_password_validation(self, driver):
        new_user = Steps()
        new_user.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_BUTTON_LOCATOR)
        new_user.wait_element(driver, REGISTRATION_FORM_TITLE_LOCATOR)
        new_user.click_to_element(driver, REGISTRATION_NAME_INPUT_LOCATOR)
        new_user.input_user_name(driver, REGISTRATION_NAME_INPUT_LOCATOR, 'BurgerDestroyer2202')
        new_user.click_to_element(driver, REGISTRATION_EMAIL_INPUT_LOCATOR)
        new_user.input_user_email(driver, REGISTRATION_EMAIL_INPUT_LOCATOR, 'BurgerD')
        new_user.click_to_element(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR)
        new_user.input_user_password(driver, REGISTRATION_PASSWORD_INPUT_LOCATOR, '1234q')
        new_user.click_to_element(driver, COMPLETE_REGISTRATION_BUTTON)
        error_message = new_user.find_element(driver, ERROR_TEXT_INPUT_LOCATOR)
        assert error_message is not None