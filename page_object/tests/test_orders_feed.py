import allure
import pytest

from page_object.helpers import create_user_and_order
from page_object.pages.main_page import MainPage

from page_object.data import URLS
from page_object.pages.my_profile_page import MyProfilePage


class TestMainFunctionality:

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_check_user_orders_history(self, login_page, is_logged_in, user_data):
        order_id = create_user_and_order(user_data, login_page)
        for browser, page in login_page.items():
            if is_logged_in:
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                profile_page = MyProfilePage(page.driver)
                profile_page.check_url(URLS['profile_page_url'])
                profile_page.click_orders_history_button()
                profile_page.check_url(URLS['order_history_page_url'])
                assert str(order_id) in profile_page.get_order_number()
