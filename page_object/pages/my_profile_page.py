import allure

from page_object.data import URLS
from page_object.locators.my_profile_page_locators import MyProfilePageLocators
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators


class MyProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на кнопку "История заказов"')
    def click_orders_history_button(self):
        self.click_to_element(MyProfilePageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Кликаем по кнопке "Выход"')
    def click_logout_button(self):
        self.click_to_element(MyProfilePageLocators.LOGOUT_BUTTON)
