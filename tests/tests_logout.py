from locators import PERSONAL_ACCOUNT_LOCATOR, LOGOUT_BUTTON_LOCATOR, MAIN_MENU_TITLE_LOCATOR, AUTH_FORM_TITLE_LOCATOR
from steps import Steps


class TestStellarBurgers:

    def test_success_logout_by_logout_button(self,driver, login):
        Steps.wait_element(driver, MAIN_MENU_TITLE_LOCATOR)
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, LOGOUT_BUTTON_LOCATOR)
        Steps.click_to_element(driver, LOGOUT_BUTTON_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        auth_page = Steps.find_element(driver, AUTH_FORM_TITLE_LOCATOR)
        assert auth_page is not None