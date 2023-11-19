import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from locators.locators import LoginPageLocators

URL = "https://www.saucedemo.com/"
user_name = 'standard_user'
password = 'secret_sauce'

@pytest.fixture(scope='function')
def chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    yield driver
    driver.close()

@pytest.fixture(scope='function')
def login_to_shop(chrome):
    driver = chrome
    page = LoginPage(driver)
    page.enter_text(LoginPageLocators.field_user_name, user_name)
    page.enter_text(LoginPageLocators.field_password, password)
    page.click(LoginPageLocators.button_login)
    yield driver