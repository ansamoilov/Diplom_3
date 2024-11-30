import allure
from page_object.helpers import generate_random_password
from page_object.locators.reset_password_page_locators import ResetPasswordPageLocators
from page_object.pages.base_page import BasePage
from page_object.pages.general_methods import GeneralMethods


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        """
        Инициализирует страницу сброса пароля.

        :param driver: Экземпляр драйвера для взаимодействия с браузером
        """
        super().__init__(driver)
        self.general_methods = GeneralMethods(driver)

    @allure.step('Вводим пароль')
    def input_password(self):
        """
        Вводит случайно сгенерированный пароль в поле для ввода пароля.

        Генерируется новый пароль с помощью хелпера `generate_random_password` и вводится в поле пароля.
        """
        password = generate_random_password()
        self.wait_element_to_be_clickable(ResetPasswordPageLocators.PASSWORD_INPUT)
        self.add_text_to_element(ResetPasswordPageLocators.PASSWORD_INPUT, password)

    @allure.step('Кликаем по кнопке "Показать/скрыть пароль"')
    def toggle_password_visibility(self):
        """
        Кликает по кнопке для переключения видимости пароля.

        Этот метод позволяет показать или скрыть введенный пароль в поле ввода пароля.
        """
        self.click_to_element(ResetPasswordPageLocators.TOGGLE_PASSWORD_VISIBILITY_BUTTON)

    @allure.step('Проверка, что поле пароля подсвечено')
    def check_password_field_highlighted(self):
        """
        Проверяет, что поле ввода пароля подсвечено (активное).

        Используется для проверки, что поле ввода пароля активно после ввода данных.
        """
        return self.find_element_with_wait(ResetPasswordPageLocators.ACTIVE_PASSWORD_INPUT)
