from page_object.helpers import generate_random_password
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage
import allure


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Вводим пароль в поле ввода пароля')
    def input_password(self):
        password = generate_random_password()
        self.add_text_to_element(ResetPasswordPageLocators.PASSWORD_INPUT, password)
        input_value = self.get_value_from_element(ResetPasswordPageLocators.PASSWORD_INPUT)
        return input_value

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def toggle_password_visibility(self):
        self.click_to_element(ResetPasswordPageLocators.TOGGLE_PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Проверка, что поле пароля подсвечено')
    def check_password_field_highlighted(self):
        assert self.find_element_with_wait(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT)


