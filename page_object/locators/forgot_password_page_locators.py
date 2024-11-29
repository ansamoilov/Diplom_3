from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    # Поле ввода для электронной почты
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.text.input__textfield.text_type_main-default[name='name']")

    # Кнопка "Восстановить пароль"
    RESET_BUTTON = (By.CSS_SELECTOR,
                    "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")

    # Кнопка "Восстановить" в модальном окне
    RECOVERY_BUTTON = (By.CSS_SELECTOR,
                       "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
