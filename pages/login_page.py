
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page.base_page import BasePage
class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_error_message(self,by_locator):
        message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return message
