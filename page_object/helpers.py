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


def get_ingredients():
    """
    Отправляет запрос на получение списка ингредиентов.
    Возвращает объект ответа.
    """
    response = requests.get(URLS['ingredients_url'])
    return response


def create_order(url, token=None):
    """
    Отправляет запрос на создание заказа с использованием ингредиентов.

    :param url: URL для создания заказа
    :param token: токен авторизации (опционально)
    :return: объект ответа
    """
    response = get_ingredients()

    if response.status_code == 200:
        ingredients_data = response.json()
        ingredients = [ingredient["_id"] for ingredient in ingredients_data["data"][:2]]
        headers = {}
        if token:
            headers["Authorization"] = token
        payload = {"ingredients": ingredients}
        response = requests.post(url, json=payload, headers=headers)
        return response
        response = requests.post(url, json=payload, headers=headers)

        return response
    else:
        print("Не удалось получить ингредиенты.")
        return response


def create_user_and_order(user_data, login_page):
    """
    Создает пользователя, создает заказ и логинится этим пользователем через UI.

    :param user_data: данные пользователя, полученные из фикстуры
    :param login_page: страница логина для каждого браузера
    :return: возвращает токен пользователя и данные заказа
    """
    token = user_data[2]
    response = create_order(URLS['orders_url'], token)
    assert response.status_code == 200, f"Ошибка создания заказа: {response.text}"
    order_data = response.json()
    assert order_data.get("success") is True, "Не удалось создать заказ"
    order_id = order_data.get("order", {}).get("number")
    assert order_id, "Не получен ID заказа"
    for browser, page in login_page.items():
        email = user_data[0]
        password = user_data[1]
        page.driver.get(URLS['login_page_url'])
        page.add_text_to_element(LoginPageLocators.EMAIL_INPUT_LOGIN_PAGE, email)
        page.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_LOGIN_PAGE, password)
        page.click_on_element_js(LoginPageLocators.LOGIN_BUTTON)
    return order_id


def create_user_and_add_ingredient_to_basket(user_data, login_page):
    """
    Создает пользователя, авторизуется и добавляет ингредиент в корзину через UI.

    :param user_data: данные пользователя, полученные из фикстуры
    :param login_page: страница логина, используемая для UI-логина
    """
    for browser, page in login_page.items():
        valid_credentials_log_in(page, user_data)
    for browser, page in login_page.items():
        main_page = MainPage(page.driver)
        main_page.check_url(URLS['main_page_url'])
        main_page.drag_ingredient_to_basket()


def create_user_and_order_no_auth(user_data):
    """
    Создает пользователя, создает заказ без авторизации.

    :param user_data: данные пользователя, полученные из фикстуры
    """
    token = user_data[2]
    response = create_order(URLS['orders_url'], token)
    assert response.status_code == 200, f"Ошибка создания заказа: {response.text}"
