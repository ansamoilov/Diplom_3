import random
import string

import requests
from faker import Faker

from page_object.data import URLS
from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.main_page import MainPage

faker = Faker()


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


def create_user_credentials():
    """
    Генерирует уникальные данные пользователя для регистрации
    :return: словарь с email, password и name
    """
    return {
        "email": faker.email(),
        "password": faker.password(),
        "name": faker.first_name()
    }


def register_user(user_data):
    """
    Регистрирует пользователя. Возвращает ответ от сервера.
    :param user_data: Данные для регистрации пользователя.
    :return: Ответ от сервера.
    """
    response = requests.post(URLS['register_user_url'], json=user_data)
    return response


def delete_user(token: str):
    """
    Удаляет пользователя, используя авторизационный токен.
    :param token: Авторизационный токен пользователя.
    :return: Ответ от сервера.
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(URLS['delete_user_url'], headers=headers)
    return response


# def valid_credentials_log_in(page: MainPage):
#     """
#     Авторизует пользователя с использованием данных, сгенерированных для регистрации.
#     """
#     user_data = create_user_credentials()
#     response = register_user(user_data)
#     response_data = response.json()
#     user = response_data.get("user", {})
#     email = user.get("email")
#     password = user_data["password"]
#     page.driver.get(URLS['login_page_url'])
#     page.add_text_to_element(LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE, email)
#     page.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_LOGIN_PAGE, password)
#     page.click_on_element_js(LoginPageLocators.LOGIN_BUTTON)

def valid_credentials_log_in(page: MainPage, user_data):
    """
    Авторизует пользователя с использованием данных, сгенерированных для регистрации.
    """
    email = user_data[0]
    password = user_data[1]
    page.driver.get(URLS['login_page_url'])
    page.add_text_to_element(LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE, email)
    page.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_LOGIN_PAGE, password)
    page.click_on_element_js(LoginPageLocators.LOGIN_BUTTON)


def login_user(login_data):
    """
    Метод для логина пользователя через api
    """
    response = requests.post(URLS['login_user_url'], json=login_data)
    return response




