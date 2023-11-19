import time

from pages.produtcs_page import ProdutcsPage
from locators.locators import ProductsPageLocators
import random

def test_sorting_name_by_z_to_a(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    inventories_expected = page.get_all_elements_name(ProductsPageLocators.inventory)
    page.click(ProductsPageLocators.sort_za)
    inventories_actual = page.get_all_elements_name(ProductsPageLocators.inventory)
    inventories_expected.sort(reverse=True)
    assert inventories_actual == inventories_expected

def test_sorting_by_price_low_to_high(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    prices_expected = page.get_all_elements_name(ProductsPageLocators.price)
    page.click(ProductsPageLocators.sort_price_low_high)
    prices_expected.sort()
    prices_actual = page.get_all_elements_name(ProductsPageLocators.price)
    assert prices_actual == prices_expected

def test_sorting_by_price_high_to_low(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    prices_expected = page.get_all_elements_name(ProductsPageLocators.price)
    page.click(ProductsPageLocators.sort_price_high_low)
    prices_expected.sort(reverse=True)
    prices_actual = page.get_all_elements_name(ProductsPageLocators.price)
    assert prices_actual == prices_expected

def test_open_goods_in_new_pade(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    inventories = page.get_all_elements(ProductsPageLocators.inventory)
    inventory = random.choice(inventories)
    inventory.click()
    