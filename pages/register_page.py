import allure

from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    @allure.step('Заполняем поле "Имя"')
    def fill_in_name_field(self, user_name):
        self.add_text_to_element(RegisterPageLocators.NAME_FIELD, user_name)

    @allure.step('Заполняем поле "Email"')
    def fill_in_email_field(self, user_email):
        self.add_text_to_element(RegisterPageLocators.EMAIL_FIELD, user_email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_in_password_field(self, user_password):
        self.add_text_to_element(RegisterPageLocators.PASSWORD_FIELD, user_password)

    @allure.step('Нажимаем кнопку "Зарегистрироваться"')
    def click_register_button(self):
        self.click_to_element(RegisterPageLocators.REGISTER_BUTTON)
