import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.my_profile_page_locators import MyProfilePageLocators
from page_object.locators.order_feed_page_locators import OrderFeedPageLocators
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

    @allure.step("Тапаем на элемент истории заказов и ждем появления номера заказа в модальном окне")
    def tap_order_and_wait_for_modal(self):
        """
        Тапает на элемент из истории заказов и ожидает появления номера заказа в модальном окне.
        """
        self.find_element_with_wait(MyProfilePageLocators.ORDER_HISTORY_LIST_ITEM_LOCATOR).click()
        self.wait_for_element_to_be_present(MyProfilePageLocators.MODAL_ORDER_NUMBER_LOCATOR)
        modal_window = self.find_element_with_wait(MyProfilePageLocators.MODAL_ORDER_NUMBER_LOCATOR)
        assert modal_window.is_displayed()

    @allure.step('Кликаем на кнопку "Лента заказов", ждем номер заказа и возвращаем его текст')
    def click_order_feed_button(self):
        """
        Кликаем по кнопке "Лента заказов", ждем появления номера заказа и возвращаем текст из элемента.
        """
        self.click_to_element(OrderFeedPageLocators.ORDER_FEED_BUTTON_LOCATOR)
        self.wait_for_element_to_be_present(OrderFeedPageLocators.ORDER_NUMBER_LOCATOR)
        order_number = self.get_text_from_element(OrderFeedPageLocators.ORDER_NUMBER_LOCATOR)
        return order_number

