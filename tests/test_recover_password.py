import allure

from urls.urls import Urls


class TestRecoveryPassword:

    @allure.title('Проверка перехода по клику на ссылку "Восстановить пароль"')
    def test_click_password_reset_link(self, main_page, recovery_password_page):
        main_page.go_to_url(Urls.MAIN_PAGE_URL)
        main_page.click_login_account_button()
        recovery_password_page.click_password_reset_link()

        assert recovery_password_page.get_current_url() == Urls.RECOVER_PASSWORD_PAGE_URL
        

    @allure.title('Проверка на ввод почты и клик по кнопке "Восстановить"')
    def test_enter_email_and_click_recover(self, main_page, recovery_password_page, user_data):
        main_page.go_to_url(Urls.MAIN_PAGE_URL)
        main_page.click_login_account_button()
        recovery_password_page.click_password_reset_link()
        recovery_password_page.set_email_for_reset_password(user_data["email"])
        recovery_password_page.click_reset_button()

    @allure.title(
        "Проверка, что клик по кнопке показать/скрыть пароль делает поле активным"
    )
    def test_password_field_becomes_active_after_click_show_hide_button(
        self, main_page, recovery_password_page, user_data
    ):
        main_page.go_to_url(Urls.MAIN_PAGE_URL)
        main_page.click_login_account_button()
        recovery_password_page.click_password_reset_link()
        recovery_password_page.set_email_for_reset_password(user_data["email"])
        recovery_password_page.click_reset_button()
        recovery_password_page.click_on_show_password_button()

        assert recovery_password_page.find_input_active()
