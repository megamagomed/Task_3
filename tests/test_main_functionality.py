import allure

from urls.urls import Urls
from test_data.ingredient_data import IngredientData


class TestMainFunctionality:

    @allure.title("Проверка перехода переход по клику на «Конструктор»")
    def test_click_constructor_button(self, main_page):
        main_page.open_main_page()
        main_page.click_order_feed_button()
        main_page.click_costructor_button()
        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL

    @allure.title("Проверка переход по клику на «Лента заказов»")
    def test_click_order_feed(self, main_page):
        main_page.open_main_page()
        main_page.click_order_feed_button()
        assert main_page.get_current_url() == Urls.ORDER_FEED_PAGE_URL

    @allure.title("Проверка открытия попапа с деталями ингредиента")
    def test_click_on_ingredient_show_popup(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        assert main_page.get_ingredient_name_in_popup() == IngredientData.BUN_TITLE

    @allure.title("Проверка закрытия попапа с деталями ингредиента кликом по крестику")
    def test_close_ingredient_popup(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.close_ingredient_popup()
        assert main_page.check_ingredient_popup_closed()

    @allure.title("Проверка увеличения счетчика ингредиента")
    def test_ingredient_counter(self, main_page):
        main_page.open_main_page()
        previous_counter_value = main_page.get_ingredient_counter_value()
        main_page.add_ingredient_to_bascet()
        current_counter_value = main_page.get_ingredient_counter_value()
        assert current_counter_value > previous_counter_value

    @allure.title("Проверка оформления заказа авторизованным пользователем")
    def test_place_order_logged_in_user(self, main_page, user_login):
        main_page.open_main_page()
        main_page.add_ingredient_to_bascet()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        assert order_number != ""
