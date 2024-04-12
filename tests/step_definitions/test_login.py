import pytest
from pytest_bdd import scenarios, scenario, given, when, then
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

scenarios("../features/login.feature")  

@scenario('login.feature', 'Successful login')
def login():
    pass

# Given steps
@given("the user is on the login page")
def user_is_on_login_page(browser):
    login_page = LoginPage(browser)
    login_page.open()

# When steps
@when("the user enters valid credentials")
def user_enters_valid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.perform_login("standard_user", "secret_sauce")

@when("the user enters invalid credentials")
def user_enters_invalid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.perform_login("zzzzzzzzzzzz", "secret_sauce")

@when("the user clicks the login button")
def when_user_clicks_login_button(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()

# Then steps
@then("the user should be redirected to the products page")
def then_user_redirected_to_products_page(browser):
    products_page = ProductsPage(browser)
    products_page.assert_products_page_title()

@then("an error message should be displayed")
def then_error_message_displayed(browser):
    login_page = LoginPage(browser)
    login_page.assert_bad_login_error_message()

@then("the user should remain on the login page")
def then_user_remains_on_login_page(browser):
    login_page = LoginPage(browser)
    login_page.is_on_login_page()

@then("the error message should be <expected_text>")
def then_error_message_text(browser, expected_text):
    login_page = LoginPage(browser)
    login_page.assert_bad_login_error_message() == expected_text

@then("the login logo should be displayed")
def then_login_logo_displayed(browser):
    login_page = LoginPage(browser)
    login_page.assert_login_logo_is_visible()