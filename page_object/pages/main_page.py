import allure
from selenium.common import TimeoutException

from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.general_methods import GeneralMethods


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_methods = GeneralMethods(driver)

    @allure.step('Кликаем на кнопку "Профиль"')
    def click_profile_button(self):
        """
        Кликаем по кнопке "Профиль" на главной странице.
        """
        self.move_to_element_and_click(MainPageLocators.PROFILE_BUTTON_MAIN)

    @allure.step('Кликаем на кнопку "Конструктор"')
    def click_constructor_button(self):
        """
        Кликаем по кнопке "Конструктор" на главной странице.
        """
        self.move_to_element_and_click(MainPageLocators.CONSTRUCTOR_BUTTON_LOCATOR)

    @allure.step('Проверяем, что страница конструктора загрузилась')
    def check_constructor_page_loaded(self):
        """
        Проверяем, что страница конструктора загрузилась.
        """
        try:
            self.wait_for_element_to_be_present(MainPageLocators.CONSTRUCTOR_LOCATOR)
            return True
        except TimeoutException:
            return False

    @allure.step('Кликаем на кнопку "Лента заказов"')
    def click_order_feed_button(self):
        """
        Кликаем по кнопке "Лента заказов" на главной странице.
        """
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON_LOCATOR)

    @allure.step('Кликаем на ингредиент')
    def click_ingredient(self):
        """
        Кликаем по ингредиенту в списке.
        """
        self.move_to_element_and_click(MainPageLocators.INGREDIENT_ITEM_LOCATOR)

    @allure.step('Ожидаем модальное окно с деталями ингредиента')
    def wait_for_modal_window_to_appear(self):
        """
        Ожидаем появления модального окна с деталями ингредиента.
        """
        self.wait_for_element_to_be_present(MainPageLocators.MODAL_WINDOW_LOCATOR)

    @allure.step("Проверка, что модальное окно с деталями ингредиента видно")
    def check_modal_window_is_visible(self):
        """
        Проверяем, что модальное окно с деталями ингредиента отображается на странице.
        """
        self.wait_for_element_to_be_present(MainPageLocators.MODAL_WINDOW_LOCATOR)
        return self.check_element_is_visible(MainPageLocators.MODAL_WINDOW_LOCATOR)

    @allure.step("Закрытие модалки крестиком")
    def close_modal(self):
        """
        Закрываем модальное окно, кликнув по кнопке с крестиком.
        """
        self.driver.find_element(*MainPageLocators.MODAL_CLOSE_BUTTON).click()

    @allure.step("Проверка скрытия модалки")
    def check_is_modal_hidden(self):
        """
        Проверяем, что модальное окно скрыто.
        """
        return self.check_element_is_not_visible(MainPageLocators.MODAL_WINDOW_LOCATOR)

    @allure.step("Открытие модального окна ингредиента")
    def open_modal(self):
        """
        Открываем модальное окно ингредиента, кликая на ингредиент и ожидая его появления.
        """
        self.click_ingredient()
        self.wait_for_modal_window_to_appear()

    @allure.step("Перетаскиваем ингредиент в корзину")
    def drag_ingredient_to_basket(self):
        """
        Перетаскиваем ингредиент в корзину с помощью drag-and-drop.
        """
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_ITEM_LOCATOR, MainPageLocators.BASKET_LOCATOR)

    @allure.step("Получаем цену в корзине")
    def get_basket_price(self):
        """
        Получаем текущую цену в корзине.
        """
        return self.get_value_from_element(MainPageLocators.BASKET_PRICE_LOCATOR)

