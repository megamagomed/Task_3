import allure
import time

from test_data.urls import Urls
from test_data.user_data import UserData
from test_data.ingredient_data import IngredientData
from pages.recover_password_page import RecoveryPasswordPage
from pages.main_page import MainPage
from pages.personal_account_page import UserProfilePage

class TestMainFunctionality:

    def test_click_constructor_button(self, main_page):
        main_page.open_main_page()
        main_page.click_order_feed_button()
        main_page.click_costructor_button()
        assert main_page.get_current_url() == Urls.MAIN_PAGE_URL
    
    def test_click_order_feed(self, main_page):
        main_page.open_main_page()
        main_page.click_order_feed_button()
        assert main_page.get_current_url() == Urls.ORDER_FEED_PAGE_URL
    
    def test_click_on_ingredient_show_popup(self,main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        assert main_page.get_ingredient_name_in_popup() == IngredientData.BUN_TITLE
    
    def test_close_ingredient_popup(self, main_page):
        main_page.open_main_page()
        main_page.click_on_ingredient()
        main_page.close_ingredient_popup()
        assert main_page.check_ingredient_popup_closed()
    
    def test_ingredient_counter(self, main_page):
        main_page.open_main_page()
        previous_counter_value = main_page.get_ingredient_counter_value()
        main_page.add_ingredient_to_bascet()
        current_counter_value = main_page.get_ingredient_counter_value()
        assert current_counter_value > previous_counter_value

    def test_place_order_logged_in_user(self, main_page, user_login):
        main_page.open_main_page()
        main_page.add_ingredient_to_bascet()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        assert order_number != ""

