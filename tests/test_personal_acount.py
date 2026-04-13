import allure

from test_data.urls import Urls
from test_data.user_data import UserData
from pages.recover_password_page import RecoveryPasswordPage
from pages.main_page import MainPage
from pages.personal_account_page import UserProfilePage

class TestPersonalAccount:

    @allure.title('Переход в "Личный кабинет"')
    def test_go_to_personal_account(self,main_page, user_login, personal_account_page):
        main_page.click_user_profile_button()
        assert main_page.get_current_url() == Urls.PROFILE_PAGE_URL
    
    @allure.title('Переход на страницу "История заказов"')
    def test_go_to_order_history(self,main_page, user_login, personal_account_page):
        main_page.click_user_profile_button()
        personal_account_page.click_order_history_button()
        assert personal_account_page.get_current_url() == Urls.ORDER_HISTORY_PAGE_URL
    
    @allure.title('Переход на страницу авторизации при нажатии в ЛК кнопки "Выход"')
    def test_logout(self,main_page, user_login, personal_account_page):
        main_page.click_user_profile_button()
        personal_account_page.click_log_out_button()
        assert personal_account_page.get_current_url() == Urls.LOGIN_PAGE_URL