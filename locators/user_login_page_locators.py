from selenium.webdriver.common.by import By

class UserLoginPageLocators:
    EMAIL_FIELD = By.XPATH, "//input[@type='text' and @name='name']"
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    