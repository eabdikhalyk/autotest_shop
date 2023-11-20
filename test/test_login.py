from locators.locators import LoginPageLocators
from pages.login_page import LoginPage
from locators.locators import ProductsPageLocators

user_name = 'standard_user'
password = 'secret_sauce'
title_in_page = 'Products'
invalid_user_name = "user"
invalid_password = 'secret'
error_message_invalid_data = "Epic sadface: Username and password do not match any user in this service"
error_message_empty_user_name = "Epic sadface: Username is required"
error_message_empty_password = 'Epic sadface: Password is required'
error_message_locked_user = 'Epic sadface: Sorry, this user has been locked out.'
locked_user = 'locked_out_user'

def test_with_valid_data(chrome):
    page = LoginPage(chrome)
    page.enter_text(LoginPageLocators.field_user_name, user_name)
    page.enter_text(LoginPageLocators.field_password, password)
    page.click(LoginPageLocators.login_button)
    title = page.get_title(ProductsPageLocators.title)

    assert title == title_in_page

def test_with_invalid_data(chrome):
    page = LoginPage(chrome)
    page.enter_text(LoginPageLocators.field_user_name, invalid_user_name)
    page.enter_text(LoginPageLocators.field_password, invalid_password)
    page.click(LoginPageLocators.login_button)
    message = page.get_error_message(LoginPageLocators.error_message)

    assert message == error_message_invalid_data

def test_with_empty_user_name(chrome):
    page = LoginPage(chrome)
    page.enter_text(LoginPageLocators.field_user_name, "")
    page.enter_text(LoginPageLocators.field_password, password)
    page.click(LoginPageLocators.login_button)
    message = page.get_error_message(LoginPageLocators.error_message)

    assert message == error_message_empty_user_name

def test_with_empty_password(chrome):
    page = LoginPage(chrome)
    page.enter_text(LoginPageLocators.field_user_name,user_name)
    page.enter_text(LoginPageLocators.field_password, "")
    page.click(LoginPageLocators.login_button)
    message = page.get_error_message(LoginPageLocators.error_message)

    assert message == error_message_empty_password

def test_for_locked_user(chrome):
    page = LoginPage(chrome)
    page.enter_text(LoginPageLocators.field_user_name, locked_user)
    page.enter_text(LoginPageLocators.field_password, password)
    page.click(LoginPageLocators.login_button)
    message = page.get_error_message(LoginPageLocators.error_message)

    assert message == error_message_locked_user