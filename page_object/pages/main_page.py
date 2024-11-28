import allure

from page_object.data import URLS
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход к странице восстановления пароля')
    def go_to_forgot_password_page(self):
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)
        self.check_url(URLS['login_page_url'])


