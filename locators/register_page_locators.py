from selenium.webdriver.common.by import By


class RegisterPageLocators:
    NAME_FIELD = By.XPATH, "//input[@type='text' and @name='name']"
    EMAIL_FIELD = By.XPATH, "//label[text()='Email']/following-sibling::input"
    PASSWORD_FIELD = By.XPATH, "//input[@type='password' and @name='Пароль']"
    REGISTER_BUTTON = By.XPATH, "//button[text()='Зарегистрироваться']"
