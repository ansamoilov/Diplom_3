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

    @allure.step("Получаем номер заказа с страницы 'Мой аккаунт'")
    def get_order_number(self):
        """
        Получаем номер заказа с страницы 'Мой аккаунт'.

        :return: Номер заказа
        """
        element = self.find_element_with_wait(MyProfilePageLocators.ORDER_NUMBER_LOCATOR)
        return element.text

    @allure.step("Ожидаем, что значение order id изменится с 9999 на новый id")
    def wait_for_order_id_change(self, expected_order_id):
        """
        Ожидает, что значение в локаторе изменится с 9999 на заданный order_id.
        :param expected_order_id: Новый order_id, который должен появиться.
        """
        self.wait_for_element_text_change(MyProfilePageLocators.ORDER_NUMBER_LOCATOR_MODAL, "9999", expected_order_id)
        actual_order_id = self.get_text_from_element(MyProfilePageLocators.ORDER_NUMBER_LOCATOR_MODAL)
        assert actual_order_id == str(
            expected_order_id), f"Ожидался order_id {expected_order_id}, но получен {actual_order_id}"


