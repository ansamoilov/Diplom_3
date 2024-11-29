from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:

    TOGGLE_PASSWORD_VISIBILITY_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action svg")
    INPUT_FIELD = (By.CSS_SELECTOR, "input.input_type_text")
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, "input.input_status_active")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Введите новый пароль']")
    ACTIVE_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]//input[@type='text']")
    SAVE_BUTTON = (By.CSS_SELECTOR,
                   "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")



