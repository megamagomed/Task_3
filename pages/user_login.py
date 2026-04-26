import allure


from locators.user_login_page_locators import UserLoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class LoginUserPage(BasePage):
    @allure.step('Заполняем поле "email"')
    def fill_in_email_field(self, user_email):
        self.add_text_to_element(UserLoginPageLocators.EMAIL_FIELD, user_email)

    @allure.step('Заполняем поле "Пароль"')
    def fill_in_password_field(self, user_password):
        self.add_text_to_element(UserLoginPageLocators.PASSWORD_FIELD, user_password)

    @allure.step("Нажимаем кнопку «Войти»")
    def click_login_button(self):
        self.click_safe(UserLoginPageLocators.LOGIN_BUTTON)
        self.wait_element_invisible(MainPageLocators.MODAL_OPENED)
        