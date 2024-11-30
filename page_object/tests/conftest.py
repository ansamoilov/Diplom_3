import pytest
from selenium import webdriver
from page_object.data import URLS
from page_object.helpers import create_user_credentials, register_user, delete_user, get_ingredients
from page_object.pages.login_page import LoginPage
from page_object.pages.main_page import MainPage
from page_object.pages.forgot_password_page import ForgotPasswordPage
from page_object.pages.order_feed_page import OrderFeedPage
from page_object.pages.reset_password_page import ResetPasswordPage


@pytest.fixture(scope="function")
def drivers():
    drivers = {
        "firefox": webdriver.Firefox(),
        "chrome": webdriver.Chrome()
    }
    yield drivers
    for driver in drivers.values():
        driver.quit()


@pytest.fixture
def main_page(drivers):
    main_pages = {}
    for browser, driver in drivers.items():
        driver.get(URLS["main_page_url"])
        main_pages[browser] = MainPage(driver)
    return main_pages


@pytest.fixture
def forgot_password_page(drivers):
    forgot_password_url = URLS["forgot_password_url"]
    main_pages = {}
    for browser, driver in drivers.items():
        driver.get(forgot_password_url)
        main_pages[browser] = ForgotPasswordPage(driver)
    return main_pages


@pytest.fixture
def login_page(drivers, is_logged_in):
    if is_logged_in:
        login_url = URLS["login_page_url"]
        login_pages = {}
        for browser, driver in drivers.items():
            driver.get(login_url)
            login_pages[browser] = LoginPage(driver)
        return login_pages
    else:
        main_page_url = URLS["main_page_url"]
        main_pages = {}
        for browser, driver in drivers.items():
            driver.get(main_page_url)
            main_pages[browser] = MainPage(driver)
        return main_pages


@pytest.fixture
def reset_password_page(drivers):
    forgot_password_url = URLS["forgot_password_url"]
    reset_pages = {}
    for browser, driver in drivers.items():
        driver.get(forgot_password_url)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.click_reset_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_pages[browser] = reset_password_page
    return reset_pages


@pytest.fixture
def constructor_page(drivers):
    orders_feed_page_url = URLS['orders_feed_page_url']
    constructor_pages = {}
    for browser, driver in drivers.items():
        driver.get(orders_feed_page_url)
        constructor_pages[browser] = MainPage(driver)
    return constructor_pages


@pytest.fixture
def user_data():
    """
    Фикстура для создания пользователя, регистрации и удаления пользователя после теста.
    Генерирует уникальные данные для регистрации, возвращает почту, пароль и токен.
    """
    user_data = create_user_credentials()
    response = register_user(user_data)
    response_data = response.json()
    token = response_data.get("accessToken")
    assert token, "Токен не получен, регистрация не удалась."
    yield user_data["email"], user_data["password"], token
    delete_user(token)


@pytest.fixture(scope="function")
def feed_page(drivers):
    """
    Фикстура для открытия страницы 'Лента заказов'.
    """
    feed_pages = {}
    for browser, driver in drivers.items():
        driver.get(URLS['orders_feed_url'])
        feed_pages[browser] = OrderFeedPage(driver)
    return feed_pages



