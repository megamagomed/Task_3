from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDERS_FEED_TITLE = By.XPATH, '//h1[text()="Лента заказов"]'
    ORDER_STRUCTURE = By.XPATH, '//p[text()="Cостав"]'
    ORDERS = By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]"
    ORDER = By.XPATH, "//a[contains(@class,'OrderHistory_link')]"
    ORDER_BURGER_NAME = By.XPATH, "//a[contains(@class,'OrderHistory_link')]//h2"
    BURGER_NAME_IN_MODAL = By.XPATH, "//section[contains(@class,'Modal_modal_opened')]//h2"
    TOTAL_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p"
    DAILY_ORDER_COUNT = By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDER_IN_PROGRESS = By.XPATH,  "//ul[contains(@class,'OrderFeed_orderListReady')]//li[contains(@class,'text_type_digits-default')]"
    ORDER_NUMBERS_IN_ORDER_FEED = By.XPATH, "//div[contains(@class,'OrderHistory_textBox')]/p[1]"
