import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    """Определяет поведение драйвера для тестового браузера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
