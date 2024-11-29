import random
import string

from page_object.data import URLS
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage


def generate_random_email(domain="example.com"):
    """
    Генерирует случайный email с указанным доменом.
    :param domain: Домен для email. По умолчанию используется "example.com".
    :return: Случайный email.
    """
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@{domain}"


def generate_random_password(length=12):
    """
    Генерирует случайный пароль, который включает буквы, цифры и спецсимволы.
    :param length: Длина пароля. По умолчанию 12 символов.
    :return: Случайно сгенерированный пароль.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def valid_credentials_log_in(page: BasePage):
    page.driver.get(URLS['login_page_url'])
    email = "anton_samoilov_14_123@yandex.ru"
    password = "14123!"
    page.add_text_to_element(LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE, email)
    page.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_LOGIN_PAGE, password)
    page.click_on_element_js(LoginPageLocators.LOGIN_BUTTON)

