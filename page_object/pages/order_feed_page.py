import allure

from page_object.data import URLS
from page_object.helpers import generate_random_email
from page_object.locators.order_feed_page_locators import OrderFeedPageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators
from page_object.pages.general_methods import GeneralMethods


class OrderFeedPage(BasePage):
    @allure.step("Получаем номера заказов из раздела 'В работе'")
    def get_in_progress_order_numbers(self):
        """
        Получаем все номера заказов, которые находятся в разделе 'В работе'.

        :return: Список номеров заказов
        """
        self.find_elements_with_wait(OrderFeedPageLocators.ORDER_FEED_ORDER_LIST_ITEM_LOCATOR)
        order_numbers = self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_ORDER_LIST_ITEM_LOCATOR)
        return order_numbers

    def get_current_counter_value(self):
        """
        Получаем текущее значение счетчика на странице "Лента заказов".
        :return: Текущее значение счетчика в виде числа.
        """
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_COUNTER_LOCATOR, 20)
        updated_counter_value = self.get_text_from_element(OrderFeedPageLocators.ORDER_FEED_COUNTER_LOCATOR)
        return updated_counter_value

    def open_feed_page(self):
        self.open_url_via_js(URLS['orders_feed_url'])
