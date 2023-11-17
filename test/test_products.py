import time

from pages.produtcs_page import ProdutcsPage
from locators.locators import ProductsPageLocators
def test_sorting_name_by_z_to_a(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    inventories_expected = page.get_all_elements(ProductsPageLocators.inventory)
    page.click(ProductsPageLocators.sort_za)
    inventories_actual = page.get_all_elements(ProductsPageLocators.inventory)
    inventories_expected.sort(reverse=True)
    assert inventories_actual == inventories_expected

def test_sorting_by_price_low_to_high(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    prices_expected = page.get_all_elements(ProductsPageLocators.price)
    page.click(ProductsPageLocators.sort_price_low_high)
    prices_expected.sort()
    prices_actual = page.get_all_elements(ProductsPageLocators.price)
    assert prices_actual == prices_expected