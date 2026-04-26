from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    ORDER_HISTORY_BUTTON = By.LINK_TEXT, 'История заказов'
    LOGOUT_BUTTON = By.XPATH, ".//button[text()='Выход']"
    ENABLED_ORDER_HISTORY_BUTTON = By.XPATH, '//a[contains(@class,"Account_link_active")]'
    ORDER_NUMBERS_IN_ORDER_HISTORY = By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[1]"