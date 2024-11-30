import allure
import pytest

from page_object.helpers import create_user_and_add_ingredient_to_basket
from page_object.pages.main_page import MainPage

from page_object.data import URLS
from page_object.pages.my_profile_page import MyProfilePage


class TestMainFunctionality:
    @pytest.mark.parametrize("is_logged_in", [False])
    def test_go_to_constructor_page(self, constructor_page, is_logged_in):
        for browser, page in constructor_page.items():
            page.click_constructor_button()
            assert page.check_constructor_page_loaded()

    @allure.title('Проверка перехода по клику на "Лента заказов"')
    @allure.description('Тест проверяет, что после клика на кнопку "Лента заказов" происходит переход на страницу с лентой заказов')
    def test_go_to_orders_feed_page(self, main_page):
        for browser, page in main_page.items():
            page.click_order_feed_button()
            page.check_url(URLS['orders_feed_page_url'])

    def test_ingredient_modal_window(self, main_page):
        for browser, page in main_page.items():
            page.click_ingredient()
            page.wait_for_modal_window_to_appear()
            assert page.check_modal_window_is_visible()

    @allure.title("Закрытие модального окна")
    @allure.description("Проверка закрытия модального окна крестиком")
    def test_open_and_close_modal(self, main_page):
        for browser, page in main_page.items():
            page.open_modal()
            page.close_modal()
            assert page.check_is_modal_hidden(), "Модальное окно не скрыто после закрытия"

    @allure.title("Перетаскивание ингредиента в корзину и проверка изменения цены")
    @allure.description(
        "Тест проверяет, что при перетаскивании ингредиента из меню в корзину, цена в корзине изменяется.")
    def test_drag_and_drop_ingredient_to_basket(self, main_page):
        for browser, page in main_page.items():
            page.drag_ingredient_to_basket()
            basket_price = page.get_basket_price()
            assert basket_price != "0"

    @allure.title("Отображение заказа в истории заказов")
    @allure.description(
        "Тест проверяет, что после создания заказа он отображается в истории заказов пользователя.")
    @pytest.mark.parametrize("is_logged_in", [True])
    def test_create_user_and_order_with_ui_login_and_place_order(self, login_page, is_logged_in, user_data):
        create_user_and_add_ingredient_to_basket(user_data, login_page)
        for browser, page in login_page.items():
            main_page = MainPage(page.driver)
            main_page.check_url(URLS['main_page_url'])
            main_page.click_place_order_button()
            order_id = main_page.wait_for_order_id_to_change()
            main_page.close_and_wait_for_modal_to_disappear()
            main_page.click_profile_button()
            profile_page = MyProfilePage(page.driver)
            profile_page.click_orders_history_button()
            profile_page.check_url(URLS['order_history_page_url'])
            assert order_id in profile_page.get_order_number()


