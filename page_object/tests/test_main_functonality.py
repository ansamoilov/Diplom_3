import allure
import pytest

from page_object.pages.main_page import MainPage

from page_object.data import URLS


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
            assert page.check_url(URLS['orders_feed_page_url'])

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
