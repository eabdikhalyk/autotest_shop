from test_cart import add_goods_to_cart
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
