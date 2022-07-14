from baseapp import BasePage
from locators import SearchLocators


class SearchHelper(BasePage):
    """Описывает эмуляции действий пользователя на веб-странице"""
    def enter_word(self, word):
        search_field = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_suggest_list(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)

    def check_navigation_bar(self):
        all_list = self.find_elements(
            SearchLocators.LOCATOR_YANDEX_NAVIGATION_BAR, time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def find_first_result(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_RESULT, time=2)

    def go_to_pictures_page(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_PICTURES, time=2)

    def open_first_category(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_OPEN_CATEGORY, time=2)
