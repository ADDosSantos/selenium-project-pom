import time
from selenium.webdriver.remote.webdriver import WebDriver
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage
from tests.pages.item_page import ItemPage
from tests.pages.shopping_cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage
from pytest_bdd import scenarios, given, when, then


@given('the user is logged in with valid credentials')
def user_is_logged_in_with_valid_credentials(browser: WebDriver, flag_headless):
    # user logs in
    login_page = LoginPage(browser)
    login_page.open(flag_headless)
    login_page.perform_login("standard_user", "secret_sauce")
    login_page.click_login_button()
    products_page = ProductsPage(browser)
    products_page.assert_products_page_title()

@given('the user has added a random number of items to the cart')
def the_user_adds_random_items_to_cart(browser: WebDriver, shopping_list):
     # Adding random items to cart
    products_page = ProductsPage(browser)
    products_page.add_random_nr_items_to_cart(shopping_list)

@given('the user has navigated to the cart')
def the_user_has_navigated_to_the_cart(browser: WebDriver):
    products_page = ProductsPage(browser)
    products_page.click_icon_shopping_cart()
    cart_page = CartPage(browser)
    cart_page.assert_cart_page_title()

@given('the user begins the checkout process')
def the_user_begins_the_checkout_process(browser):
    cart_page = CartPage(browser)
    cart_page.click_checkout()
    checkout_page = CheckoutPage(browser)
    checkout_page.assert_checkout_page_title()