from page_object.pages.base_page import BasePage
from page_object.locators.general_locators import GeneralLocators


class GeneralMethods(BasePage):
    def wait_for_modal_overlay_to_disappear(self):
        """
        Ожидаем исчезновения оверлея модального окна.
        Используем базовый метод ожидания из BasePage.
        """
        self.wait_element_to_disappear(GeneralLocators.MODAL_OVERLAY)
