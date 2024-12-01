from selenium.webdriver.common.by import By


class MyProfilePageLocators:
    # Кнопка "История заказов" на странице профиля
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")

    # Кнопка "Выход" на странице профиля
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Номер заказа в истории заказов
    ORDER_NUMBER_LOCATOR = (By.XPATH, "//p[@class='text text_type_digits-default']")

    # Плитка заказа в истории заказов
    ORDER_HISTORY_LIST_ITEM_LOCATOR = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r')]")

    # Номер заказа в модальном окне
    MODAL_ORDER_NUMBER_LOCATOR = (
    By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi')]//p[contains(@class, 'text_type_digits-default')]")
