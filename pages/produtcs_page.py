from base_page.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ProdutcsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_list = []
    def get_all_elements(self, by_locator):
        inventories = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator))
        for item_name in inventories:
            self.name_list.append(item_name.text)

        return self.name_list