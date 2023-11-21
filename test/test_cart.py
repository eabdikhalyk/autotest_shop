import random
from pages.cart_page import CartPage
from locators.locators import ProductsPageLocators
from pages.produtcs_page import ProdutcsPage
from locators.locators import CartPageLocators

count_of_goods = 3

def add_goods_to_cart(driver):
    page = ProdutcsPage(driver)
    buttons = page.get_all_elements(ProductsPageLocators.add_to_cart_button)
    for i in range(0, 3):
        button = buttons[i]
        button.click()
    return driver

def test_added_goods(login_to_shop):
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    inventories = cart_page.get_all_elements(CartPageLocators.inventory)

    assert len(inventories) == count_of_goods

def test_remove_goods_from_cart(login_to_shop):
    inventories = None
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    remove_buttons = cart_page.get_all_elements(CartPageLocators.remove_buttons)
    for button in remove_buttons:
        button.click()
    try:
        inventories = cart_page.get_all_elements(CartPageLocators.inventory)
    except:
        pass

    assert inventories is None