import time
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.item_page import ItemPage
from pages.shopping_cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pytest_bdd import (
    scenarios,
    given,
    scenario,
    then,
    when,
    parsers,
)

scenarios("../features/checkout_your_information.feature")

# Given steps

@given("the user is on the checkout: Your Information page")
def user_is_on_checkout_your_information_page(browser):
    checkout_page = CheckoutPage(browser)
    checkout_page.assert_checkout_page_title()


# When steps

@when(parsers.parse('the user fills in the form with the following input:\n{attr_table}'))
def user_fills_in_checkout_form(browser, attr_table):
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_in_checkout_form(attr_table)

@when('the user clicks the Continue button')
def user_clicks_continue(browser):
    checkout_page = CheckoutPage(browser)
    checkout_page.click_continue_checkout()



@when(parsers.parse("the user fills in the form with the partial information first name: {first_name}, last name: {last_name}, zip code: {postal_code}, and submits it"))
def user_enters_login_credentials(browser, first_name, last_name, postal_code):
    checkout_page = CheckoutPage(browser)
    checkout_page.fill_in_checkout_form_continue(first_name, last_name, postal_code)

# Then steps

@then(parsers.parse ('the following elements should be visible:\n{attr_table}'))
def the_following_elements_should_be_visible(browser, attr_table):
    checkout_page = CheckoutPage(browser)
    checkout_page.validate_presence_checkout_information_page_elements(attr_table)

@then('the user sees his previously chosen items')
def the_following_elements_should_be_visible(browser, shopping_list):
    cart_page = CartPage(browser)
    cart_page.validate_presence_of_selected_items(shopping_list)


@then(parsers.parse('the error message "{error_message}" should be displayed'))
def user_enters_login_credentials(browser, error_message):
    checkout_page = CheckoutPage(browser)
    checkout_page.validate_error_message_as_expected(error_message)


@then("the user should be redirected to the checkout: Overview page")
def user_is_on_checkout_your_information_page(browser):
    checkout_page_overview = CheckoutPage(browser)
    checkout_page_overview.assert_checkout_overview_page_title()

@when("the user clicks the Cancel button")
@then("the user clicks the Cancel button")
def user_clicks_cancel_button(browser):
    checkout_page_your_info = CheckoutPage(browser)
    checkout_page_your_info.click_btn_cancel()

@then("the user should be redirected to Your Cart page")
def user_redirected_your_cart(browser):
    cart_page = CartPage(browser)
    cart_page.assert_cart_page_title()

@when("the user clicks the Cart icon")
@then("the user clicks the Cart icon")
def user_clicks_cancel_button(browser):
    checkout_page_your_info = CheckoutPage(browser)
    checkout_page_your_info.click_icon_cart()