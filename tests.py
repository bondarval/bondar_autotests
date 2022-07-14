from baseapp import BasePage
from searchpage import SearchHelper


def test_yandex_search(browser):
    """Тестирование текстового поиска"""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    suggest_list = yandex_main_page.check_suggest_list()
    assert suggest_list in BasePage.base_url
    yandex_main_page.click_on_the_search_button()
    first_result = yandex_main_page.find_first_result()
    assert first_result.get_attribute("URL") == "https://tensor.ru/"


def test_yandex_picture_search(browser):
    """Тестирование поиска по изображению"""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    elements = yandex_main_page.check_navigation_bar()
    assert "Картинки" in elements
    pictures = yandex_main_page.go_to_pictures_page()
    pictures.click()
    assert pictures.get_attribute("URL") == "https://yandex.ru/images/"
    category = yandex_main_page.open_first_category()
