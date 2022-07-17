import logging

from selenium.common import TimeoutException

from searchpage import SearchHelper, PictureSearchHelper

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger()


def test_yandex_search(browser):
    """Тестирование текстового поиска"""
    LOGGER.info('Поиск по слову "Тензор" от Яндекса')
    yandex_main_page = SearchHelper(browser)
    LOGGER.info('Переход на главную страницу Яндекса')
    try:
        yandex_main_page.go_to_site()
    except TimeoutException:
        LOGGER.error('Главная страница Яндекса не найдена!')
    LOGGER.info('Ввод ключевого слова в поисковую строку')
    try:
        yandex_main_page.enter_word("Тензор")
    except TimeoutException:
        LOGGER.error('Поисковая строка не обнаружена!')
    LOGGER.info('Проверка появления списка подсказок')
    try:
        yandex_main_page.check_suggest_list()
    except TimeoutException:
        LOGGER.error('Список подсказок не появился!')
    LOGGER.info('Инициализация процедуры поиска')
    try:
        yandex_main_page.click_on_the_search_button()
    except TimeoutException:
        LOGGER.error('Не нажата кнопка поиска!')
    LOGGER.info('Поиск первого результата')
    try:
        yandex_main_page.find_first_result()
    except TimeoutException:
        LOGGER.error('Первый результат не обнаружен!')
    LOGGER.info('Проверка первого результата')
    try:
        yandex_main_page.check_first_result()
    except TimeoutException:
        LOGGER.error('Первый результат не релевантен запросу!')


def test_yandex_picture_search(browser):
    """Тестирование поиска по изображению"""
    LOGGER.info('Поиск изображения от Яндекса')
    yandex_main_page = PictureSearchHelper(browser)
    LOGGER.info('Переход на главную страницу Яндекса')
    try:
        yandex_main_page.go_to_site()
    except TimeoutException:
        LOGGER.error('Главная страница Яндекса не найдена!')
    LOGGER.info('Поиск раздела "Яндекс.Картинки" на главной странице')
    try:
        yandex_main_page.find_pictures_page()
    except TimeoutException:
        LOGGER.error('Раздел "Яндекс.Картинки" не обнаружен!')
    LOGGER.info('Переход в раздел "Яндекс.Картинки"')
    try:
        yandex_main_page.find_pictures_page().click()
    except TimeoutException:
        LOGGER.error('Раздел "Яндекс.Картинки" не обнаружен!')
    LOGGER.info('Открытие первой категории картинок в разделе')
    try:
        yandex_main_page.open_first_category()
    except TimeoutException:
        LOGGER.error('Первая категория картинок не обнаружена!')
    LOGGER.info('Проверка текста поиска первой категории картинок')
    try:
        yandex_main_page.check_category_search_text()
    except TimeoutException:
        LOGGER.error('Текст поиска не обнаружен!')
    except AssertionError:
        LOGGER.error('Текст поиска не совпадает с текстом в поисковой строке!')
    LOGGER.info('Открытие первой картинки в категории')
    try:
        yandex_main_page.open_first_picture()
    except TimeoutException:
        LOGGER.error('Картинка не открывается!')
    LOGGER.info('Проверка смены картинки при нажатии кнопки "вперед"')
    id_image1 = yandex_main_page.open_picture().get_attribute('src')
    try:
        yandex_main_page.find_forward_button().click()
    except TimeoutException:
        LOGGER.error('Кнопка "вперед" не обнаружена!')
    id_image2 = yandex_main_page.open_picture().get_attribute('src')
    assert (
        id_image1 != id_image2,
        'Картинка не изменилась после нажатия кнопки "вперед"!')
    LOGGER.info('Проверка смены картинки при нажатии кнопки "назад"')
    try:
        yandex_main_page.find_back_button().click()
    except TimeoutException:
        LOGGER.error('Кнопка "назад" не обнаружена!')
    id_image3 = yandex_main_page.open_picture().get_attribute('src')
    assert (
        id_image1 == id_image3,
        'Кнопка "назад" не возвращает на предыдущую картинку!')
