from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_object.locators.forgot_password_page_locators import ForgotPasswordPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                locator))
        return self.driver.find_element(*locator)

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def wait_not_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(locator)
        )

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of(element)
        )
        return element

    def format_locators(self, locator, index):
        method, locator = locator
        locator = locator.format(index)
        return method, locator

    def check_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url))
        assert url in self.driver.current_url

    def switch_browser_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_value_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.get_attribute("value")

    def wait_element_to_disappear(self, overlay_locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(overlay_locator)
        )

    def wait_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

