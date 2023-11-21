from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_text_of_element(self, by_locator) -> str:
        title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        return title

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def get_all_elements(self, by_locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        return elements