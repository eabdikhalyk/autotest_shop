import random
from pages.produtcs_page import ProdutcsPage
from locators.locators import ProductsPageLocators
from locators.locators import ViewPageLocators

def test_open_goods_in_new_pade(login_to_shop):
    page = ProdutcsPage(login_to_shop)
    inventories = page.get_all_elements(ProductsPageLocators.inventory)
    inventory = random.choice(inventories)
    inventory.click()
    image_of_item = page.get_element(ViewPageLocators.image_of_item)
    name_of_item = page.get_element(ViewPageLocators.name_of_item)
    description_of_item = page.get_element(ViewPageLocators.description_of_item)

    assert image_of_item is not None
    assert name_of_item is not None
    assert description_of_item is not None