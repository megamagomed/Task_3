from selenium.webdriver.common.by import By

class RecoverPasswordLocators:
    FORGOT_PASSWORD_LINK = By.XPATH, '//a[contains(@href, "/forgot-password")]'
    EMAIL_INPUT_FIELD = By.XPATH, '//label[text()="Email"]/following-sibling::input'
    RECOVER_PASSWORD_BUTTON = By.XPATH, '//button[text()="Восстановить"]'
    PASSWORD_INPUT_FIELD = (By.NAME, 'Введите новый пароль')
    SHOW_PASSWORD_BUTTON =  (By.XPATH, '//div[contains(@class,"input__icon-action")]')
    INPUT_ACTIVE = By.CSS_SELECTOR, '.input.input_status_active'