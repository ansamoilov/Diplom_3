from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.button_button_type_primary__1O7Bx")
    PROFILE_BUTTON_MAIN = (By.XPATH, "//p[text()='Личный Кабинет']")

