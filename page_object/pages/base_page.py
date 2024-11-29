import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, timeout=10):
        """
        Ожидаем появления элемента, соответствующего локатору, и возвращаем его.

        :param locator: Локатор элемента
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        :return: Найденный элемент
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator, timeout=10):
        """
        Ожидаем появления всех элементов, соответствующих локатору, и возвращаем их.

        :param locator: Локатор для поиска элементов
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        :return: Список найденных элементов
        """
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        """
        Кликаем по элементу, дождавшись его кликабельности.

        :param locator: Локатор элемента для клика
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def wait_element_to_disappear(self, locator, timeout=10):
        """
        Ожидаем исчезновения элемента по локатору.

        :param locator: Локатор элемента
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        """
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def move_to_element_and_click(self, locator):
        """
        Прокручиваем страницу до элемента и кликаем по нему, если элемент скрыт.

        :param locator: Локатор элемента, по которому нужно кликнуть
        """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def click_on_element_js(self, locator):
        """
        Кликаем по элементу с помощью JavaScript.

        :param locator: Локатор элемента, по которому нужно кликнуть
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        """
        Прокручиваем страницу до элемента.

        :param locator: Локатор элемента, до которого нужно прокрутить страницу
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def add_text_to_element(self, locator, text):
        """
        Находим элемент и вводим в него текст.

        :param locator: Локатор элемента
        :param text: Текст для ввода
        """
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        """
        Получаем текст из элемента.

        :param locator: Локатор элемента
        :return: Текст элемента
        """
        return self.find_element_with_wait(locator).text

    def check_url(self, url, timeout=20, delay=2):
        """
        Проверяем, что текущий URL соответствует ожидаемому, с дополнительной задержкой перед проверкой.

        :param url: Ожидаемый URL
        :param timeout: Время ожидания (по умолчанию 20 секунд)
        :param delay: Задержка перед проверкой URL (по умолчанию 2 секунды)
        """
        time.sleep(delay)
        #задержка, на случай если url обновится не сразу
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
        assert url in self.driver.current_url

    def wait_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def move_to_element_and_click(self, locator):
        """
        Наводит курсор на элемент и кликает по нему.
        :param locator: Локатор элемента, по которому нужно кликнуть.
        """
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def get_value_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.get_attribute("value")

# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def find_element_with_wait(self, locator):
#         WebDriverWait(self.driver, 10).until(
#             expected_conditions.visibility_of_element_located(
#                 locator))
#         return self.driver.find_element(*locator)
#
#     def click_to_element(self, locator):
#         WebDriverWait(self.driver, 5).until(
#             expected_conditions.element_to_be_clickable(locator))
#         self.driver.find_element(*locator).click()
#
#     def wait_not_element(self, locator):
#         WebDriverWait(self.driver, 10).until(
#             expected_conditions.invisibility_of_element_located(locator)
#         )
#
#     def add_text_to_element(self, locator, text):
#         self.find_element_with_wait(locator).send_keys(text)
#
#     def get_text_from_element(self, locator):
#         return self.find_element_with_wait(locator).text
#
#     def scroll_to_element(self, locator):
#         element = self.find_element_with_wait(locator)
#         self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
#         WebDriverWait(self.driver, 10).until(
#             expected_conditions.visibility_of(element)
#         )
#         return element
#
#     def format_locators(self, locator, index):
#         method, locator = locator
#         locator = locator.format(index)
#         return method, locator
#
#     def check_url(self, url, timeout=10):
#         WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
#         assert url in self.driver.current_url
#
#     def switch_browser_tab(self):
#         self.driver.switch_to.window(self.driver.window_handles[-1])
#

#
#     def wait_element_to_disappear(self, overlay_locator, timeout=30):
#         WebDriverWait(self.driver, timeout).until(
#             EC.invisibility_of_element_located(overlay_locator)
#         )
#
#     def wait_element_to_be_clickable(self, locator, timeout=10):
#         WebDriverWait(self.driver, timeout).until(
#             EC.element_to_be_clickable(locator)
#         )
#
#     def wait_element_not_present(self, locator, timeout=30):
#         WebDriverWait(self.driver, timeout).until_not(
#             EC.presence_of_element_located(locator)
#         )

