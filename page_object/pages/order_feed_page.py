import allure

from page_object.locators.order_feed_page_locators import OrderFeedPageLocators
from page_object.pages.base_page import BasePage


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

    @allure.step("Получаем все счетчики в ленте заказов'")
    def get_order_feed_counters(self):
        """
        Находит все элементы, соответствующие локатору ORDER_FEED_COUNTER_LOCATOR,
        и возвращает их список.
        """
        elements = self.find_all_elements(OrderFeedPageLocators.ORDER_FEED_COUNTER_LOCATOR)
        return elements

    @allure.step("Получаем значения счетчиков в ленте заказов")
    def get_counter_value(self, index):
        """
        Получает текст счетчика из списка.
        :param index: индекс счетчика (начиная с 0)
        """
        counters = self.get_order_feed_counters()
        if isinstance(index, int):
            return counters[index].text
        else:
            raise TypeError("Index must be an integer")
