from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # ссылка "Зарегистрироваться" на странице входа
    REGISTER_BUTTON_LOGIN_PAGE = (By.XPATH, "//button[text()='Зарегистрироваться']") # кнопка "Зарегистрироваться" на странице входа
    EMAIL_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Email"]/parent::div/input') # инпут почты на странице входа
    PASSWORD_INPUT_LOGIN_PAGE = (By.XPATH, '//label[text()="Пароль"]/parent::div/input') # инпут пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка "Войти" на странице входа
