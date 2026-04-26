from selenium.webdriver.common.by import By
from test_data.ingredient_data import IngredientData


class MainPageLocators:
    LOGIN_PROFILE_BUTTON = By.XPATH, ".//button[text()='Войти в аккаунт']"
    OVERLAY = By.XPATH, '//div[contains(@class, "Modal_modal_overlay")]'
    ORDER_HISTORY_BUTTON = By.LINK_TEXT, "История заказов"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//a[@href="/account"]'
    MAIN_PAGE_TITLE = By.XPATH, "//h1[text()='Соберите бургер']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']/parent::a"
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']/parent::a"
    BUN = By.XPATH, f"//p[text()='{IngredientData.BUN_TITLE}']"
    INGREDIENT_POPUP = By.XPATH, '//h2[text()="Детали ингредиента"]'
    CLOSE_INGREDIENT_POPUP = By.XPATH, '//button[contains(@class,"close")]'
    INGREDIENT_COUNTER = By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]'
    CONSTRUCTOR_BASKET = (
        By.XPATH,
        "//div[contains(@class,'constructor-element_pos_top')]",
    )
    INGREDIENT_NAME_IN_POPUP = (
        By.XPATH,
        "//div[contains(@class,'Modal_modal__contentBox')]//p[contains(@class,'text_type_main-medium')]",
    )
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_ID = By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]'
    ORDER_ID_TITLE = By.XPATH, '//p[text()="идентификатор заказа"]'
    CLOSE_ORDER_POPUP = By.XPATH, '//button[contains(@class,"close")]'
    ORDER_POPUP = By.XPATH, "//section[contains(@class,'Modal_modal_opened')]"
    MODAL_OPENED = (By.XPATH,".//div[contains(@class, 'Modal_modal_opened__') and contains(@class, 'Modal_modal__')]",
    )
