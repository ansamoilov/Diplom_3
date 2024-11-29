from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='name']")
    RESET_BUTTON = (By.CSS_SELECTOR,
                    "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    RECOVERY_BUTTON = (By.CSS_SELECTOR,
                       "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")


