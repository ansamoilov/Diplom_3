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
        """
        Ожидаем, что элемент станет кликабельным.

        :param locator: Локатор элемента
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        """
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_value_from_element(self, locator):
        """
        Получаем значение атрибута "value" элемента.

        :param locator: Локатор элемента
        :return: Значение атрибута "value"
        """
        element = self.find_element_with_wait(locator)
        return element.get_attribute("value")

    def wait_for_element_to_be_present(self, locator, timeout=10):
        """
        Ожидаем появления элемента на странице.

        :param locator: Локатор элемента, который нужно найти
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        """
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def check_element_is_visible(self, locator, timeout=10):
        """
        Проверяем, виден ли элемент.

        :param locator: Локатор элемента
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        :return: True, если элемент видим, иначе False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def check_element_is_not_visible(self, locator, timeout=10):
        """
        Проверяем, скрыт ли элемент.

        :param locator: Локатор элемента
        :param timeout: Время ожидания (по умолчанию 10 секунд)
        :return: True, если элемент скрыт, иначе False
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def drag_and_drop_element(self, locator_from, locator_to):
        """
        Метод для выполнения drag-and-drop перетаскивания элемента с одного места на другое.

        :param locator_from: Локатор исходного элемента
        :param locator_to: Локатор целевого элемента
        """
        self.check_element_is_visible(locator_from)
        self.check_element_is_visible(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            // Создаем событие dragstart
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            // Создаем событие dragenter
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            // Создаем событие dragover
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            // Создаем событие drop
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            // Создаем событие dragend
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    def wait_for_element_text_change(self, locator, initial_value="9999", timeout=30):
        """
        Ожидаем, что текст элемента изменится с начального значения на любое другое значение.
        """
        WebDriverWait(self.driver, timeout).until(
            lambda driver: self.get_text_from_element(locator) != initial_value
        )
        actual_value = self.get_text_from_element(locator)
        assert actual_value != initial_value, f"Ожидалось изменение значения с {initial_value}, но оно осталось прежним"

    def find_all_elements(self, locator, timeout=20):
        """
        Находит все элементы, соответствующие локатору, и возвращает их список.

        :param locator: Локатор, по которому нужно найти элементы.
        :param timeout: Время ожидания видимости элементов (по умолчанию 20 секунд).
        :return: Список элементов.
        """
        elements = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
        return elements
