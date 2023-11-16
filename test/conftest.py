import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
URL = "https://www.saucedemo.com/"

@pytest.fixture(scope='function')
def chrome():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options,service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    yield driver
    driver.close()


@pytest.fixture(scope='function')
def login_to_shop():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))

    yield driver
    driver.close()
