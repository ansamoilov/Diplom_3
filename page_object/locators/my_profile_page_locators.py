from selenium.webdriver.common.by import By


class MyProfilePageLocators:
    # Кнопка "История заказов" на странице профиля
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")

    # Кнопка "Выход" на странице профиля
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
