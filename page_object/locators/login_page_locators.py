from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Кнопка "Забыли пароль?" на странице входа
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")

    # Инпут для ввода почты на странице входа
    EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    # Инпут для ввода пароля на странице входа
    PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
