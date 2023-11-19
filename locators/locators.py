from selenium.webdriver.common.by import By

class LoginPageLocators():
    field_user_name = (By.ID,'user-name')
    field_password = (By.ID,'password')
    button_login = (By.ID,'login-button')
    error_message = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

class ProductsPageLocators():
    title = (By.CLASS_NAME,'title')
    inventory = (By.CLASS_NAME,'inventory_item_name')
    price = (By.CLASS_NAME,'inventory_item_price')
    sort_za = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[2]')
    sort_price_low_high = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    sort_price_high_low = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[4]')