from baseapp import BasePage
from locators import SearchLocators


class SearchHelper(BasePage):
    """Описывает эмуляции действий для текстового поиска"""
    def enter_word(self, word):
        """Ищет поисковую строку и вводит ключевое слово в неё"""
        search_field = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        """Нажимает на кнопку поиска"""
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def check_suggest_list(self):
        """Проверяет, появляется ли список подсказок к строке поиска"""
        suggest_list = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)
        assert self.locate_visibility(
            SearchLocators.LOCATOR_YANDEX_SUGGEST_LIST, time=2)
        return suggest_list

    def find_first_result(self):
        """Проверяет наличие первого результата в выдаче поиска"""
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_RESULT, time=2)

    def check_first_result(self):
        """Проверяет релевантность первого результата введенному ключеввому слову"""
        first_result = self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_RESULT, time=2)
        assert self.find_element(
            SearchLocators.LOCATOR_YANDEX_RESULT_EXISTS, time=2)
        return first_result


class PictureSearchHelper(BasePage):
    """Описывает эмуляции действий для поиска по изображению"""
    def find_pictures_page(self):
        """Ищет вкладку поиска картинок"""
        pictures = self.find_element(
            SearchLocators.LOCATOR_YANDEX_PICTURES, time=2)
        assert self.find_element(
            SearchLocators. LOCATOR_YANDEX_PICTURES_PAGE, time=2)
        return pictures

    def open_first_category(self):
        """Открывает первую категорию поиска по картинкам"""
        return self.switch_windows()

    def check_category_search_text(self):
        """
        Проверяет соответствие запроса в поисковой строке
        названию открытой категории
        """
        search_text = self.find_element(
            SearchLocators.LOCATOR_YANDEX_CATEGORY_TEXT, time=2)
        text1 = search_text.text
        search_text.click()
        text_in_search_box = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD, time=2)
        text2 = text_in_search_box.get_attribute("value")
        assert text1 == text2
        return search_text

    def open_first_picture(self):
        """Открывает первую картинку категории"""
        picture = self.find_element(
            SearchLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=2)
        picture.click()
        assert self.locate_visibility(
            SearchLocators.LOCATOR_YANDEX_OPENED_IMAGE, time=2)
        return picture

    def open_picture(self):
        """Открывает картинку"""
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_OPENED_IMAGE)

    def find_forward_button(self):
        """Ищет кнопку перехода на картинку вперед"""
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_FORWARD_BUTTON, time=2)

    def find_back_button(self):
        """Ищет кнопку перехода на картинку назад"""
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_BACK_BUTTON, time=2)
