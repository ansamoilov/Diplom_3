import allure

from page_object.data import URLS
from page_object.pages.base_page import BasePage
from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.general_methods import GeneralMethods


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.general_methods = GeneralMethods(driver)

    @allure.step('Переход к странице восстановления пароля')
    def go_to_forgot_password_page(self):
        self.click_to_element(MainPageLocators.LOGIN_BUTTON)
        self.check_url(URLS['login_page_url'])

    @allure.step('Кликаем на кнопку "Личный кабинет"')
    def click_profile_button(self):
        self.general_methods.wait_for_modal_overlay_to_disappear()
        self.scroll_to_element(MainPageLocators.PROFILE_BUTTON_MAIN)
        self.wait_element_to_be_clickable(MainPageLocators.PROFILE_BUTTON_MAIN)
        self.click_to_element(MainPageLocators.PROFILE_BUTTON_MAIN)

