import allure
from page_object.pages.base_page import BasePage
from page_object.locators.general_locators import GeneralLocators


class GeneralMethods(BasePage):

    @allure.step('Ожидаем исчезновения оверлея модального окна')
    def wait_for_modal_overlay_to_disappear(self):
        """
        Ожидаем исчезновения оверлея модального окна.
        """
        self.wait_element_to_disappear(GeneralLocators.MODAL_OVERLAY)
