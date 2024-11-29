import allure
import pytest

from page_object.data import URLS


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Тест проверяет переход на страницу восстановления пароля по кнопке "Восстановить пароль"')
    @pytest.mark.parametrize("is_logged_in", [True])
    def test_go_to_forgot_password_page(self, login_page, is_logged_in):
        for browser, page in login_page.items():
            page.click_forgot_password_button()
            current_url = page.driver.current_url
            expected_url = URLS['forgot_password_url']
            assert current_url == expected_url, \
                f"Ожидался URL {expected_url}, но был {current_url}"

    @allure.title('Проверка ввода случайной почты для восстановления пароля')
    @allure.description('Тест проверяет ввод случайной почты в поле восстановления пароля')
    def test_input_random_email(self, forgot_password_page):
        for browser, page in forgot_password_page.items():
            random_email, input_value = page.input_email()
            assert input_value == random_email, f"Ожидалась почта {random_email}, но было {input_value}"

    @allure.title('Проверка клика по кнопке «Восстановить»')
    @allure.description('Тест проверяет клик по кнопке восстановления пароля и переход на страницу сброса пароля')
    def test_click_reset_button(self, forgot_password_page):
        for browser, page in forgot_password_page.items():
            page.click_reset_button()
            page.check_url(URLS['reset_password_url'])

    @allure.title('Проверка подсветки поля пароля при клике по кнопке "Показать/скрыть пароль"')
    @allure.description(
        'Тест проверяет, что клик по кнопке "Показать/скрыть пароль" делает поле активным и подсвечивает его')
    def test_toggle_password_visibility_and_highlight(self, reset_password_page):
        for browser, page in reset_password_page.items():
            page.input_password()
            page.toggle_password_visibility()
            page.check_password_field_highlighted()
