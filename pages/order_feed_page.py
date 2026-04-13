import allure
from pages.base_page import BasePage
# from pages.main_page import MainPage
# from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedLocators
# from locators.personal_account_locators import PersonalAccountLocators
# from selenium.webdriver.support import expected_conditions as EC
from test_data.urls import Urls


class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу ленты заказов')
    def open_order_feed_page(self):
        self.go_to_url(Urls.ORDER_FEED_PAGE_URL)

    @allure.step('Открыть заказ в ленте')
    def click_to_order(self):
        self.click_to_element(OrderFeedLocators.ORDER)
        self.find_element_with_wait(OrderFeedLocators.ORDER_STRUCTURE)

    @allure.step('Получить название бургера в карточке заказа')
    def get_burger_name_in_order(self):
        return self.get_text_from_element(OrderFeedLocators.ORDER_BURGER_NAME)

    @allure.step('Получить название бургера в попапе заказа')
    def get_burger_name_in_popup(self):
        return self.get_text_from_element(OrderFeedLocators.BURGER_NAME_IN_MODAL)

    @allure.step('Получить все номера заказов из ленты')
    def get_all_order_numbers_from_feed(self):
        order_numbers = self.find_elements_with_wait(
            OrderFeedLocators.ORDER_NUMBERS_IN_ORDER_FEED
        )
        return [order.text for order in order_numbers]

    @allure.step('Получить значение счетчика заказов')
    def get_counter_value(self, counter_type):
        counters = {
            "all_time": OrderFeedLocators.TOTAL_ORDER_COUNT,
            "today": OrderFeedLocators.DAILY_ORDER_COUNT,
        }
        return int(self.get_text_from_element(counters[counter_type]))

    @allure.step('Получить номер заказа в разделе "В работе"')
    def get_order_in_progress(self):
        return self.get_text_from_element(OrderFeedLocators.ORDER_IN_PROGRESS)

    @allure.step('Добавить 0 в номер заказа и дождаться его появления в разделе "В работе"')
    def add_leading_zero_to_order_number(self, order_number):
        order_with_zero = f"0{order_number}"
        self.wait_for_text_to_be_present_in_element(
            OrderFeedLocators.ORDER_IN_PROGRESS, order_with_zero
        )
        return order_with_zero
