from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Определяет базовые методы для работы с веб-страницей"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        """Находит на странице первый элемент с указанным локатором"""
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located(locator),
            message=f"Нет элемента с указателем {locator}")

    def find_elements(self, locator, time=10):
        """Находит на странице все элементы с указанным локатором"""
        return WebDriverWait(self.driver, time).until(
            ec.presence_of_all_elements_located(locator),
            message=f"Нет элементов с указателем {locator}")

    def locate_visibility(self, locator, time=10):
        """
        Определяет, отображается  ли на странице
        первый элемент с указанным локатором
        """
        return WebDriverWait(self.driver, time).until(
            ec.visibility_of_element_located(locator),
            message=f"Не отображается элемент с указателем {locator}")

    def switch_windows(self):
        """Переключает окна текущей сесссии"""
        window_before = self.driver.window_handles[0]
        window_after = self.driver.window_handles[1]
        return self.driver.switch_to.window(window_after)

    def go_to_site(self):
        """Переходит на указанный веб-адрес"""
        return self.driver.get(self.base_url)
