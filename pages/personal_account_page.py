import allure

from locators.personal_account_locators import PersonalAccountLocators
from locators.user_login_page_locators import UserLoginPageLocators
from pages.base_page import BasePage


class UserProfilePage(BasePage):

    @allure.step("Переход в историю заказов")
    def click_order_history_button(self):
        self.click_to_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        return self.find_element_with_wait(
            PersonalAccountLocators.ENABLED_ORDER_HISTORY_BUTTON
        )

    @allure.step("Выход из аккаунта")
    def click_log_out_button(self):
        self.click_to_element(PersonalAccountLocators.LOGOUT_BUTTON)
        return self.find_element_with_wait(UserLoginPageLocators.LOGIN_TITLE)

    @allure.step("Получить все номера заказов из истории заказов")
    def get_all_order_numbers_from_history(self):
        order_numbers = self.find_elements_with_wait(
            PersonalAccountLocators.ORDER_NUMBERS_IN_ORDER_HISTORY
        )
        return [order.text for order in order_numbers]
