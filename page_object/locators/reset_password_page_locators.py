from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    # Кнопка для отображения/скрытия пароля
    TOGGLE_PASSWORD_VISIBILITY_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action svg")

    # Поле для ввода текста (например, почты или имени пользователя)
    INPUT_FIELD = (By.CSS_SELECTOR, "input.input_type_text")

    # Активное поле ввода текста (например, в случае успешной фокусировки)
    INPUT_FIELD_ACTIVE = (By.CSS_SELECTOR, "input.input_status_active")

    # Поле для ввода нового пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @name='Введите новый пароль']")

    # Активное поле для ввода пароля, отображающееся при отображении пароля в виде текста
    ACTIVE_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]//input[@type='text']")

    # Кнопка "Сохранить" на странице сброса пароля
    SAVE_BUTTON = (By.CSS_SELECTOR,
                   "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
