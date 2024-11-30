import allure
import pytest

from page_object.helpers import create_user_and_order
from page_object.pages.main_page import MainPage

from page_object.data import URLS
from page_object.pages.my_profile_page import MyProfilePage
from page_object.pages.order_feed_page import OrderFeedPage


class TestOrdersFeed:

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_open_modal_by_click_on_order(self, login_page, is_logged_in, user_data):
        create_user_and_order(user_data, login_page)
        for browser, page in login_page.items():
            if is_logged_in:
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                profile_page = MyProfilePage(page.driver)
                profile_page.check_url(URLS['profile_page_url'])
                profile_page.click_orders_history_button()
                profile_page.check_url(URLS['order_history_page_url'])
                profile_page.tap_order_and_wait_for_modal()

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_orders_displayed_in_feed(self, login_page, is_logged_in, user_data):
        create_user_and_order(user_data, login_page)
        for browser, page in login_page.items():
            if is_logged_in:
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                profile_page = MyProfilePage(page.driver)
                profile_page.check_url(URLS['profile_page_url'])
                profile_page.click_orders_history_button()
                profile_page.check_url(URLS['order_history_page_url'])
                order_id = profile_page.get_order_number()
                order_id_feed = profile_page.click_order_feed_button()
                assert order_id == order_id_feed, f'{order_id_feed} и {order_id} не совпадают'

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_order_appears_in_in_progress_after_creation(self, login_page, is_logged_in, user_data):
        order_id = create_user_and_order(user_data, login_page)
        for browser, page in login_page.items():
            if is_logged_in:
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_order_feed_button()
                order_feed_page = OrderFeedPage(page.driver)
                in_progress_orders = order_feed_page.get_in_progress_order_numbers()
                assert str(order_id) in in_progress_orders, f"Ожидалось, что заказ с номером {order_id} будет найден в разделе 'В работе', но не найден."

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_order_appears_in_all_time_counter(self, login_page, is_logged_in, user_data, feed_page):
        for browser, page in feed_page.items():
            initial_counter_value = page.get_current_counter_value()
            if is_logged_in:
                create_user_and_order(user_data, login_page)
                main_page = MainPage(page.driver)
                main_page.click_order_feed_button()
                order_feed_page = OrderFeedPage(page.driver)
                # order_feed_page.open_feed_page()
                updated_counter_value = order_feed_page.get_current_counter_value()
                assert updated_counter_value > initial_counter_value, f"Значение {initial_counter_value} не обновилось"


