import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedLocators
from locators.personal_account_locators import PersonalAccountLocators
from test_data.urls import Urls


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.go_to_url(Urls.MAIN_PAGE_URL)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_login_account_button(self):
        self.wait_element_invisible(MainPageLocators.OVERLAY)
        self.click_to_element_js(MainPageLocators.LOGIN_PROFILE_BUTTON)
        return self.get_current_url()

    @allure.step('Перейти в личный кабинет')
    def click_user_profile_button(self):
        self.wait_element_invisible(MainPageLocators.OVERLAY)
        self.click_to_element_js(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.find_element_with_wait(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Перейти в конструктор')
    def click_costructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_with_wait(MainPageLocators.MAIN_PAGE_TITLE)

    @allure.step('Перейти в ленту заказов')
    def click_order_feed_button(self):
        self.wait_element_invisible(MainPageLocators.OVERLAY)
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.find_element_with_wait(OrderFeedLocators.ORDERS_FEED_TITLE)

    @allure.step('Открыть детали ингредиента')
    def click_on_ingredient(self):
        self.wait_element_invisible(MainPageLocators.OVERLAY)
        self.click_to_element(MainPageLocators.BUN)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Получить название ингредиента в попапе')
    def get_ingredient_name_in_popup(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_NAME_IN_POPUP)

    @allure.step('Закрыть попап ингредиента')
    def close_ingredient_popup(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_POPUP)
        self.wait_element_invisible(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_to_bascet(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN)
        self.drag_and_drop_element(
            MainPageLocators.BUN, MainPageLocators.CONSTRUCTOR_BASKET
        )

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter_value(
        self,
    ):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('Проверить, что попап ингредиента закрыт')
    def check_ingredient_popup_closed(self):
        return self.wait_element_invisible(MainPageLocators.INGREDIENT_POPUP)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_order_button(self):
        self.wait_element_invisible(MainPageLocators.OVERLAY)
        self.click_to_element_js(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_text_from_element(MainPageLocators.ORDER_ID)

    @allure.step('Дождаться обновления номера заказа')
    def wait_until_order_number_updated(self):
        self.find_element_with_wait(MainPageLocators.ORDER_ID)
        self.wait.until(
            lambda driver: self.get_text_from_element(MainPageLocators.ORDER_ID).strip()
            not in ("", "9999")
        )

    @allure.step('Закрыть попап заказа')
    def close_order_popup(self):
        self.click_to_element_js(MainPageLocators.CLOSE_ORDER_POPUP)
    
    @allure.step('Создать заказ и получить номер созданного заказа')
    def create_order_and_get_order_number(self):
        self.open_main_page()
        self.add_ingredient_to_bascet()
        self.click_order_button()
        order_number = self.get_order_number
        self.wait_until_order_number_updated()
        self.close_order_popup()
        return order_number