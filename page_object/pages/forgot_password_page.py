import allure

from page_object.helpers import generate_random_email
from page_object.pages.base_page import BasePage
from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from page_object.pages.general_methods import GeneralMethods


class ForgotPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_methods = GeneralMethods(driver)

    @allure.step('Клик на кнопку "Восстановить пароль"')
    def click_forgot_password_button(self):
        """
        Кликаем по кнопке для перехода на страницу восстановления пароля.

        Ожидаем, что модальное оверлейное окно исчезнет, после чего прокручиваем страницу и кликаем по кнопке.
        """
        self.general_methods.wait_for_modal_overlay_to_disappear()
        self.scroll_to_element(ForgotPasswordPageLocators.RESET_BUTTON)
        self.wait_element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
        self.click_to_element(ForgotPasswordPageLocators.RESET_BUTTON)

    @allure.step('Вводим случайную почту в поле восстановления пароля')
    def input_email(self):
        """
        Вводим случайный email в поле восстановления пароля.

        Генерируем случайный email и вводим его в поле. Также возвращаем email и значение в поле.
        """
        random_email = generate_random_email()
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, random_email)
        input_value = self.get_value_from_element(ForgotPasswordPageLocators.EMAIL_INPUT)
        return random_email, input_value

    @allure.step('Кликаем по кнопке "Восстановить"')
    def click_reset_button(self):
        """
        Кликаем на кнопку "Восстановить" для начала процесса восстановления пароля.

        Ожидаем, что модальное оверлейное окно исчезнет и кликаем по кнопке с помощью JavaScript.
        """
        self.general_methods.wait_for_modal_overlay_to_disappear()
        self.wait_element_to_be_clickable(ForgotPasswordPageLocators.RESET_BUTTON)
        self.click_on_element_js(ForgotPasswordPageLocators.RESET_BUTTON)
