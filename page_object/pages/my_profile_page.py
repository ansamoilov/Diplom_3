import allure
from page_object.locators.my_profile_page_locators import MyProfilePageLocators
from page_object.pages.base_page import BasePage


class MyProfilePage(BasePage):

    def __init__(self, driver):
        """
        Инициализирует страницу профиля пользователя.

        :param driver: Экземпляр драйвера для взаимодействия с браузером
        """
        super().__init__(driver)

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_orders_history_button(self):
        """
        Кликаем на кнопку "История заказов" на странице профиля.

        Это действие открывает раздел с историей заказов пользователя.
        """
        self.click_to_element(MyProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_logout_button(self):
        """
        Кликаем на кнопку "Выход" на странице профиля.

        Это действие выходит из текущей учетной записи пользователя.
        """
        self.click_to_element(MyProfilePageLocators.LOGOUT_BUTTON)
