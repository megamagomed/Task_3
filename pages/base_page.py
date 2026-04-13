import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.wait = WebDriverWait(self.driver, self.timeout)
    
    def go_to_url(self, url):
        self.driver.get(url)
    
    def get_current_url(self):
        return self.driver.current_url

    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        element =self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    

    def click_to_element_js(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def wait_element_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))
    
    def find_elements_with_wait(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
        
    def drag_and_drop_element(self, ingredient_locator, bascet_locator):
        source = self.find_element_with_wait(ingredient_locator)
        target = self.find_element_with_wait(bascet_locator)
        drag_and_drop(self.driver,  source, target)
    
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locator))
    
    def wait_url_to_be(self, url):
        return self.wait.until(EC.url_to_be(url))
    
    def wait_for_text_to_be_present_in_element(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
