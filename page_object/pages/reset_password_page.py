from page_object.helpers import generate_random_password
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage
import allure

from page_object.pages.general_methods import GeneralMethods


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_methods = GeneralMethods(driver)

    @allure.step('Вводим пароль')
    def input_password(self):
        password = generate_random_password()
        self.wait_element_to_be_clickable(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.add_text_to_element(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def toggle_password_visibility(self):
        self.click_to_element(ResetPasswordPageLocators.TOGGLE_PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Проверка, что поле пароля подсвечено')
    def check_password_field_highlighted(self):
        assert self.find_element_with_wait(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT)


