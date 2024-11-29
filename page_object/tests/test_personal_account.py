import pytest

from page_object.data import URLS
from page_object.helpers import valid_credentials_log_in
from page_object.pages.main_page import MainPage


class TestPersonaLAccount:
    @pytest.mark.parametrize("is_logged_in", [False, True])
    def test_login_button_behavior(self, login_page, is_logged_in):
        for browser, page in login_page.items():
            if is_logged_in:
                valid_credentials_log_in(page)
                page.check_url(URLS['main_page_url'])
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                page.check_url(URLS['profile_page_url'])
            else:
                main_page = MainPage(page.driver)
                main_page.click_profile_button()
                page.check_url(URLS['login_page_url'])



