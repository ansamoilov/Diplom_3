import allure

from page_object.locators.login_page_locators import LoginPageLocators
from page_object.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем по кнопке "Забыли пароль?"')
    def click_forgot_password_button(self):
        self.click_to_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
