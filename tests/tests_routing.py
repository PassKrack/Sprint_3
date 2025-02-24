from locators import PERSONAL_ACCOUNT_LOCATOR, AUTH_FORM_TITLE_LOCATOR, AUTH_BUTTON_LOCATOR, LOGO_LOCATOR, \
    MAIN_MENU_TITLE_LOCATOR, CONSTRUCTOR_BUTTON_LOCATOR
from steps import Steps


class TestStellarBurgersRouting:

    def test_success_go_to_the_personal_account_page(self, driver, setup_login):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        auth_button = Steps.find_element(driver, AUTH_BUTTON_LOCATOR)
        assert auth_button is not None

    def test_success_routing_from_personal_account_by_logo(self, driver, setup_login):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, LOGO_LOCATOR)
        menu_title = Steps.find_element(driver, MAIN_MENU_TITLE_LOCATOR)
        assert menu_title is not None

    def test_success_routing_from_personal_account_by_constructor(self, driver, setup_login):
        Steps.click_to_element(driver, PERSONAL_ACCOUNT_LOCATOR)
        Steps.wait_element(driver, AUTH_FORM_TITLE_LOCATOR)
        Steps.click_to_element(driver, CONSTRUCTOR_BUTTON_LOCATOR)
        menu_title = Steps.find_element(driver, MAIN_MENU_TITLE_LOCATOR)
        assert menu_title is not None