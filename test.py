from searchpage import SearchHelper, PictureSearchHelper


def test_yandex_search(browser):
    """Тестирование текстового поиска"""
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_suggest_list()
    yandex_main_page.click_on_the_search_button()
    yandex_main_page.find_first_result()
    yandex_main_page.check_first_result()


def test_yandex_picture_search(browser):
    """Тестирование поиска по изображению"""
    yandex_main_page = PictureSearchHelper(browser)
    yandex_main_page.go_to_site()
    pictures = yandex_main_page.find_pictures_page()
    pictures.click()
    yandex_main_page.open_first_category()
    yandex_main_page.check_category_search_text()
    yandex_main_page.open_first_picture()
    id_image1 = yandex_main_page.open_picture().get_attribute('src')
    forward_button = yandex_main_page.find_forward_button()
    forward_button.click()
    id_image2 = yandex_main_page.open_picture().get_attribute('src')
    assert (
        id_image1 != id_image2,
        'Картинка не изменилась после нажатия кнопки "вперед"!')
    back_button = yandex_main_page.find_back_button()
    back_button.click()
    id_image3 = yandex_main_page.open_picture().get_attribute('src')
    assert (
        id_image1 == id_image3,
        'Кнопка "назад" не возвращает на предыдущую картинку!')
