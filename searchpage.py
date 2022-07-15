from baseapp import BasePage
from locators import SearchLocators


class SearchHelper(BasePage):
    """Описывает эмуляции действий для текстового поиска"""
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
        suggest_list = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)
        assert self.locate_visibility(
            SearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)
        return suggest_list

    def find_first_result(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_RESULT, time=2)

    def check_first_result(self):
        first_result = self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_RESULT, time=2)
        assert self.find_element(
            SearchLocators.LOCATOR_YANDEX_RESULT_EXISTS, time=2)
        return first_result


class PictureSearchHelper(BasePage):
    """Описывает эмуляции действий для поиска по изображению"""
    def find_pictures_page(self):
        pictures = self.find_element(
            SearchLocators.LOCATOR_YANDEX_PICTURES, time=2)
        assert self.find_element(
            SearchLocators. LOCATOR_YANDEX_PICTURES_PAGE, time=2)
        return pictures

    def open_first_category(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_OPEN_CATEGORY, time=2).click()

    def check_category_search_text(self):
        search_text = self.find_element(
            SearchLocators.LOCATOR_YANDEX_CATEGORY_TEXT, time=2)
        assert search_text in self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        return search_text

    def open_first_picture(self):
        picture = self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=2)
        picture.click()
        assert self.locate_visibility(
            SearchLocators.LOCATOR_YANDEX_OPENED_IMAGE, time=2)
        return picture

    def open_picture(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_OPENED_IMAGE)

    def find_forward_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_FORWARD_BUTTON, time=2)

    def find_back_button(self):
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_BACK_BUTTON, time=2)
