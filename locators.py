from selenium.webdriver.common.by import By


class SearchLocators:
    """Определяет необходимые для тестирования элементы веб-страницы"""
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_SUGGEST_LIST = (
        By.CSS_SELECTOR,
        '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible'
    )
    LOCATOR_YANDEX_FIRST_RESULT = (By.CSS_SELECTOR, "h2>span")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_PICTURES = (By.CSS_SELECTOR, '[data-id="images"]')
    LOCATOR_YANDEX_OPEN_CATEGORY = (
        By.CSS_SELECTOR,
        '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > img'
    )
    LOCATOR_YANDEX_CATEGORY_TEXT = (
        By.CSS_SELECTOR,
        '.PopularRequestList-Item.PopularRequestList-Item_pos_0 > a > div.PopularRequestList-SearchText'
    )
    LOCATOR_YANDEX_FIRST_IMAGE = (
        By.XPATH,
        '//body/div[5]/div[1]/div[1]/div[1]/div/div[1]/div/a'
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
        '.MediaViewer-View.MediaViewer_theme_fiji-View > div > img'
    )
