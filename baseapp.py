from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Определяет базовые методы для работы с веб-страницей"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator),
            message=f"Не удалось найти элемент по указателю {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_all_elements_located(locator),
            message=f"Не удалось найти элементы по указателю {locator}")

    def locate_visibility(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            ec.visibility_of_element_located(locator),
            message=f"Не удалось найти элементы по указателю {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
