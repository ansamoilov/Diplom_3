import allure

from page_object.data import URLS
from page_object.helpers import generate_random_email
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_forgot_password_button(self):
        self.scroll_to_element(ForgotPasswordPageLocators.RESET_BUTTON)
        self.click_to_element(ForgotPasswordPageLocators.RESET_BUTTON)

    @allure.step('Вводим случайную почту в поле восстановления пароля')
    def input_email(self):
        random_email = generate_random_email()
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, random_email)
        input_value = self.get_value_from_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        return random_email, input_value

    # @allure.step('Кликаем по кнопке "Восстановить"')
    # def click_reset_button(self):
    #     self.wait_for_modal_to_disappear()
    #     self.click_to_element(ForgotPasswordPageLocators.RESET_BUTTON)
    #     self.find_element_with_wait(ResetPasswordPageLocators.SAVE_BUTTON)
    #     self.check_url(URLS['reset_password_url'])

    @allure.step('Ожидаем, пока модальное окно исчезнет')
    def wait_for_modal_to_disappear(self, timeout=10):
        self.wait_element_to_disappear(ForgotPasswordPageLocators.MODAL_OVERLAY, timeout)

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_reset_button(self):
        self.wait_for_modal_to_disappear()
        self.wait_element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
        self.click_to_element(ForgotPasswordPageLocators.RESET_BUTTON)
        self.find_element_with_wait(ResetPasswordPageLocators.SAVE_BUTTON)
