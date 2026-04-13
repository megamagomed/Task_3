import pytest
import allure
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.personal_account_page import UserProfilePage
from pages.recover_password_page import RecoveryPasswordPage
from pages.user_login import LoginUserPage
from pages.register_page import RegisterPage
from pages.order_feed_page import OrderFeedPage
from test_data.urls import Urls
from locators.main_page_locators import MainPageLocators
from locators.user_login_page_locators import UserLoginPageLocators
from helpers import (
    generate_new_user_email,
    generate_new_user_name,
    generate_new_user_password,
)
from locators.register_page_locators import RegisterPageLocators

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        with allure.step("Открытие браузера Chrome"):
            driver = ChromeDriver()
    else:
        with allure.step("Открытие браузера Firefox"):
            firefox_options = FirefoxOptions()
            driver = FirefoxDriver(options=firefox_options)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def login_page(driver):
    return LoginUserPage(driver)


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)


@pytest.fixture
def recovery_password_page(driver):
    return RecoveryPasswordPage(driver)


@pytest.fixture
def personal_account_page(driver):
    return UserProfilePage(driver)


@pytest.fixture
def create_user(register_page, user_data):
    register_page.go_to_url(Urls.REGISTER_PAGE_URL)
    register_page.fill_in_name_field(user_data["name"])
    register_page.fill_in_email_field(user_data["email"])
    register_page.fill_in_password_field(user_data["password"])
    register_page.click_register_button()
    return user_data


@pytest.fixture
def user_login(create_user, main_page, login_page):
    main_page.go_to_url(Urls.MAIN_PAGE_URL)
    main_page.click_login_account_button()
    login_page.find_element_with_wait(UserLoginPageLocators.LOGIN_BUTTON)
    login_page.fill_in_email_field(create_user["email"])
    login_page.fill_in_password_field(create_user["password"])
    
    login_page.click_login_button()
    # main_page.find_element_with_wait(MainPageLocators.CREATE_ORDER_BUTTON)
    # login_page.wait_url_to_be(Urls.MAIN_PAGE_URL)
    return login_page


@pytest.fixture
def user_data():
    data = {
        "name": generate_new_user_name(),
        "email": generate_new_user_email(),
        "password": generate_new_user_password(),
    }
    return data