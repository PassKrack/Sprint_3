from locators import PERSONAL_ACCOUNT_LOCATOR, AUTH_FORM_TITLE_LOCATOR, AUTH_EMAIL_INPUT_LOCATOR, \
    AUTH_PASSWORD_INPUT_LOCATOR, AUTH_BUTTON_LOCATOR, GO_TO_AUTH_BUTTON_LOCATOR, REGISTRATION_BUTTON_LOCATOR, \
    REGISTRATION_FORM_TITLE_LOCATOR, GO_TO_AUTH_FORM_BUTTON_LOCATOR, FORGOT_PASSWORD_BUTTON_LOCATOR, \
    FORGOT_PASSWORD_PAGE_TITLE_LOCATOR, LOGOUT_BUTTON_LOCATOR
from steps import Steps


class TestStellarBurgers:

    def test_success_auth_from_personal_account(self, driver):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
        Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, 'BurgerD')
        Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
        Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, '1234qweR)')
        Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        quit_button = Steps.find_element(driver, LOGOUT_BUTTON_LOCATOR)
        assert quit_button is not None



    def test_success_auth_from_main_page(self, driver):
        Steps.click_to_element(driver, GO_TO_AUTH_BUTTON_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
        Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, 'BurgerD')
        Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
        Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, '1234qweR)')
        Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        quit_button = Steps.find_element(driver, LOGOUT_BUTTON_LOCATOR)
        assert quit_button is not None



    def test_success_auth_from_registration_page(self, driver):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, REGISTRATION_BUTTON_LOCATOR)
        Steps.wait_element(driver, REGISTRATION_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, GO_TO_AUTH_FORM_BUTTON_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
        Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, 'BurgerD')
        Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
        Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, '1234qweR)')
        Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        quit_button = Steps.find_element(driver, LOGOUT_BUTTON_LOCATOR)
        assert quit_button is not None



    def test_success_auth_from_forgot_password_page(self, driver):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver,FORGOT_PASSWORD_BUTTON_LOCATOR)
        Steps.wait_element(driver, FORGOT_PASSWORD_PAGE_TITLE_LOCATOR)
        Steps.click_to_element(driver, GO_TO_AUTH_FORM_BUTTON_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, AUTH_EMAIL_INPUT_LOCATOR)
        Steps.input_user_email(driver, AUTH_EMAIL_INPUT_LOCATOR, 'BurgerD')
        Steps.click_to_element(driver, AUTH_PASSWORD_INPUT_LOCATOR)
        Steps.input_user_password(driver, AUTH_PASSWORD_INPUT_LOCATOR, '1234qweR)')
        Steps.click_to_element(driver, AUTH_BUTTON_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        quit_button = Steps.find_element(driver, LOGOUT_BUTTON_LOCATOR)
        assert quit_button is not None