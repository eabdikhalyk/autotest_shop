from selenium.webdriver.common.by import By

class LoginPageLocators():
    field_user_name = (By.ID,'user-name')
    field_password = (By.ID,'password')
    login_button = (By.ID, 'login-button')
    error_message = (By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

class ProductsPageLocators():
    title = (By.CLASS_NAME,'title')
    inventory = (By.CLASS_NAME,'inventory_item_name')
    price = (By.CLASS_NAME,'inventory_item_price')
    sort_za = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[2]')
    sort_price_low_high = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[3]')
    sort_price_high_low = (By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select/option[4]')
    add_to_cart_button = (By.CLASS_NAME, 'btn_primary.btn_small.btn_inventory')
    cart_count = (By.CLASS_NAME,'shopping_cart_badge')
    link_to_cart = (By.CLASS_NAME,'shopping_cart_link')

class ViewPageLocators():
    image_of_item = (By.CLASS_NAME, 'inventory_details_img')
    name_of_item = (By.CLASS_NAME, 'inventory_details_name.large_size')
    description_of_item = (By.CLASS_NAME, 'inventory_details_desc.large_size')

class CartPageLocators():
    inventory = (By.CLASS_NAME, 'inventory_item_name')
    remove_buttons = (By.CLASS_NAME, 'btn.btn_secondary.btn_small.cart_button')
    checkout_button = (By.CLASS_NAME,'btn.btn_action.btn_medium.checkout_button')

class CheckoutPageLocators():
    first_name = (By.ID,'first-name')
    last_name = (By.ID,'last-name')
    postal_code = (By.ID,'postal-code')
    continue_button = (By.ID,'continue')
    payment_info = (By.CLASS_NAME,'summary_info_label')
    inventory_price = (By.CLASS_NAME,'inventory_item_price')
    item_total = (By.CLASS_NAME,'summary_subtotal_label')