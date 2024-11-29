import pytest

from page_object.data import URLS
from page_object.helpers import valid_credentials_log_in
from page_object.pages.main_page import MainPage
from page_object.pages.my_profile_page import MyProfilePage


class TestPersonaLAccount:
    @pytest.mark.parametrize("is_logged_in", [False, True])
    def test_personal_account_button_redirects_to_account_page(self, login_page, is_logged_in):
        for browser, page in login_page.items():
            if is_logged_in:
                valid_credentials_log_in(page)
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                page.check_url(URLS['profile_page_url'], delay=5)
            else:
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                page.check_url(URLS['login_page_url'])

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_go_to_orders_history(self, login_page, is_logged_in):
        for browser, page in login_page.items():
            if is_logged_in:
                valid_credentials_log_in(page)
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                profile_page = MyProfilePage(page.driver)
                profile_page.check_url(URLS['profile_page_url'])
                profile_page.click_orders_history_button()
                profile_page.check_url(URLS['order_history_page_url'])

    @pytest.mark.parametrize("is_logged_in", [True])
    def test_logout_from_account(self, login_page, is_logged_in):
        for browser, page in login_page.items():
            if is_logged_in:
                valid_credentials_log_in(page)
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                profile_page = MyProfilePage(page.driver)
                profile_page.check_url(URLS['profile_page_url'])
                profile_page.click_logout_button()
                profile_page.check_url(URLS['login_page_url'])
