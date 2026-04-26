import allure
from pages.base_page import BasePage
from locators.recover_password_locators import RecoverPasswordLocators


class RecoveryPasswordPage(BasePage):
    @allure.step('Нажать на "Восстановить пароль"')
    def click_password_reset_link(self):
        self.click_to_element(RecoverPasswordLocators.FORGOT_PASSWORD_LINK)
        return self.get_current_url()

    @allure.step('Ввод емейл в поле "Email"')
    def set_email_for_reset_password(self, email):
        self.add_text_to_element(RecoverPasswordLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_reset_button(self):
        self.click_to_element(RecoverPasswordLocators.RECOVER_PASSWORD_BUTTON)

    @allure.step('Ввод пароля в поле "Пароль"')
    def set_password_for_reset_password(self, password):
        self.add_text_to_element(RecoverPasswordLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step("Нажать на кнопку Показать/скрыть пароль")
    def click_on_show_password_button(self):
        self.click_to_element(RecoverPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Найти активное поле Пароль")
    def find_input_active(self):
        return self.find_element_with_wait(RecoverPasswordLocators.INPUT_ACTIVE)
