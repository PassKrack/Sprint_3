from locators import MAIN_MENU_TITLE_LOCATOR, ROLLS_CHAPTER_LOCATOR, \
    SAUCES_CHAPTER_LOCATOR, INDICATION_SELECT_LOCATOR, FILLINGS_CHAPTER_LOCATOR
from steps import Steps


class TestStellarBurgersConstructor:

    def test_success_rolls_chapter_selected(self, driver, setup_login):
        Steps.wait_element(driver, MAIN_MENU_TITLE_LOCATOR)
        Steps.click_to_element(driver, SAUCES_CHAPTER_LOCATOR)
        Steps.wait_element(driver, INDICATION_SELECT_LOCATOR)
        Steps.click_to_element(driver, ROLLS_CHAPTER_LOCATOR)
        Steps.wait_element(driver, INDICATION_SELECT_LOCATOR)
        rolls_chapter = Steps.find_element(driver, INDICATION_SELECT_LOCATOR)
        assert rolls_chapter.text == 'Булки'

    def test_success_sauces_chapter_selected(self, driver, setup_login):
        Steps.wait_element(driver, MAIN_MENU_TITLE_LOCATOR)
        Steps.click_to_element(driver, SAUCES_CHAPTER_LOCATOR)
        Steps.wait_element(driver,INDICATION_SELECT_LOCATOR)
        sauce_chapter = Steps.find_element(driver, INDICATION_SELECT_LOCATOR)
        assert sauce_chapter.text == 'Соусы'

    def test_success_fillings_chapter_selected(self, driver, setup_login):
        Steps.wait_element(driver, MAIN_MENU_TITLE_LOCATOR)
        Steps.click_to_element(driver, FILLINGS_CHAPTER_LOCATOR)
        Steps.wait_element(driver,INDICATION_SELECT_LOCATOR)
        fillings_chapter = Steps.find_element(driver, INDICATION_SELECT_LOCATOR)
        assert fillings_chapter.text == 'Начинки'