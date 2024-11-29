from selenium.webdriver.common.by import By


class MyProfilePageLocators:
    ORDERS_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

