
from selenium.webdriver.common.by import By

class LoginPageLocators():
    field_user_name = (By.ID,'user-name')
    field_password = (By.ID,'password')
    button_login = (By.ID,'login-button')
    error_message = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

class ProductsPageLocators():
    title =   (By.CLASS_NAME,'title')