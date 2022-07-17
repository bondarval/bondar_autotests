from selenium.webdriver.common.by import By


class SearchLocators:
    """Определяет необходимые для тестирования элементы веб-страницы"""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.CSS_SELECTOR, ".search2__input input")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST_LIST = (
        By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_FIRST_RESULT = (By.CSS_SELECTOR, "li.serp-item")
    LOCATOR_YANDEX_RESULT_EXISTS = (
        By.CSS_SELECTOR,
        "a[href='https://tensor.ru/']")
    LOCATOR_YANDEX_PICTURES = (By.CSS_SELECTOR, '[data-id="images"]')
    LOCATOR_YANDEX_PICTURES_PAGE = (
        By.CSS_SELECTOR,
        "a[href='https://yandex.ru/images/?utm_source=main_stripe_big']")
    LOCATOR_YANDEX_OPEN_CATEGORY = (
        By.CSS_SELECTOR,
        ".PopularRequestList-Item")
    LOCATOR_YANDEX_CATEGORY_TEXT = (
        By.CSS_SELECTOR,
        '.PopularRequestList-SearchText'
    )
    LOCATOR_YANDEX_FIRST_IMAGE = (
        By.CSS_SELECTOR,
        '.serp-item__link'
    )
    LOCATOR_YANDEX_IMAGE_WINDOW = (
        By.CSS_SELECTOR,
        '.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container'
    )
    LOCATOR_YANDEX_BACK_BUTTON = (
        By.CSS_SELECTOR,
        ".MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i"
    )
    LOCATOR_YANDEX_FORWARD_BUTTON = (
        By.CSS_SELECTOR,
        ".MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i"
    )
    LOCATOR_YANDEX_OPENED_IMAGE = (
        By.CSS_SELECTOR,
        '.MMImageContainer'
    )
