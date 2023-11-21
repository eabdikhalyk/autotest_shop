import random

from pages.produtcs_page import ProdutcsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from locators.locators import ProductsPageLocators
from locators.locators import CartPageLocators
from locators.locators import CheckoutPageLocators

first_name = 'Bob'
last_name = 'Brown'
postal_code = '0001'
payment_info_expected = 'Payment Information'
complete_expected = 'Thank you for your order!'
error_message_first_name = 'Error: First Name is required'
error_message_last_name = 'Error: Last Name is required'
error_message_zip = 'Error: Postal Code is required'

def add_goods_to_cart(driver):
    driver.implicitly_wait(3)
    page = ProdutcsPage(driver)
    buttons = page.get_all_elements(ProductsPageLocators.add_to_cart_button)
    for _ in range(0, 3):
        button = random.choice(buttons)
        button.click()
    return driver


def test_checkout_from(login_to_shop):
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    cart_page.get_element(CartPageLocators.checkout_button).click()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_text(CheckoutPageLocators.first_name,text=first_name)
    checkout_page.enter_text(CheckoutPageLocators.last_name, text=last_name)
    checkout_page.enter_text(CheckoutPageLocators.postal_code,text=postal_code)
    checkout_page.click(CheckoutPageLocators.continue_button)
    payment_info_actual = checkout_page.get_element(CheckoutPageLocators.payment_info).text

    assert payment_info_actual == payment_info_expected

def test_checkout_from_without_first_name(login_to_shop):
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    cart_page.get_element(CartPageLocators.checkout_button).click()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_text(CheckoutPageLocators.first_name, text="")
    checkout_page.enter_text(CheckoutPageLocators.last_name, text=last_name)
    checkout_page.enter_text(CheckoutPageLocators.postal_code, text=postal_code)
    checkout_page.click(CheckoutPageLocators.continue_button)
    error_message = checkout_page.get_element(CheckoutPageLocators.error_message).text

    assert error_message == error_message_first_name

def test_total_price(login_to_shop):
    inventory_total_price = 0.0
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    cart_page.get_element(CartPageLocators.checkout_button).click()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_text(CheckoutPageLocators.first_name, text=first_name)
    checkout_page.enter_text(CheckoutPageLocators.last_name, text=last_name)
    checkout_page.enter_text(CheckoutPageLocators.postal_code, text=postal_code)
    checkout_page.click(CheckoutPageLocators.continue_button)
    inventory_prices = checkout_page.get_all_elements(CheckoutPageLocators.inventory_price)
    for item in inventory_prices:
         text = item.text.replace("$","")
         inventory_total_price +=float(text)
    text_in_bill = checkout_page.get_element(CheckoutPageLocators.item_total).text
    text_in_bill = text_in_bill.replace("Item total: $","")
    total_price_in_bill =  float(text_in_bill)

    assert  inventory_total_price == total_price_in_bill



def test_completion_payment(login_to_shop):
    driver = add_goods_to_cart(login_to_shop)
    page = ProdutcsPage(driver)
    page.get_element(ProductsPageLocators.link_to_cart).click()
    cart_page = CartPage(driver)
    cart_page.get_element(CartPageLocators.checkout_button).click()
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_text(CheckoutPageLocators.first_name, text=first_name)
    checkout_page.enter_text(CheckoutPageLocators.last_name, text=last_name)
    checkout_page.enter_text(CheckoutPageLocators.postal_code, text=postal_code)
    checkout_page.click(CheckoutPageLocators.continue_button)
    checkout_page.click(CheckoutPageLocators.button_finish)
    complete = checkout_page.get_text_of_element(CheckoutPageLocators.complete_header)

    assert complete == complete_expected