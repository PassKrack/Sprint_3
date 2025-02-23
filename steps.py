from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Steps:

    @staticmethod
    def click_to_element(driver, locator):
        driver.find_element(By.XPATH, locator).click()

    @staticmethod
    def wait_element(driver, locator):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))

    @staticmethod
    def wait_input_error_element(driver, locator):
        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, locator)))

    @staticmethod
    def find_element(driver, locator):
        try:
            return driver.find_element(By.XPATH, locator)
        except Exception as e:
            return None

    @staticmethod
    def input_user_name(driver, locator, name):
        driver.find_element(By.XPATH, locator).clear()
        driver.find_element(By.XPATH, locator).send_keys(name)

    @staticmethod
    def input_user_email(driver, locator, login):
        driver.find_element(By.XPATH, locator).clear()
        driver.find_element(By.XPATH, locator).send_keys(f'{login}@ya.ru')

    @staticmethod
    def input_user_password(driver, locator, password):
        driver.find_element(By.XPATH, locator).clear()
        driver.find_element(By.XPATH, locator).send_keys(password)

    @staticmethod
    def get_field_value(driver, locator):
        field_value = driver.find_element(By.XPATH, locator)
        return field_value.get_attribute("value")