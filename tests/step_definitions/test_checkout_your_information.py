import time
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.item_page import ItemPage
from pages.shopping_cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers,
)


@scenario('features\checkout_your_information.feature', 'User clicks the Cancel button')
def test_user_clicks_the_cancel_button():
    """User clicks the Cancel button."""
    raise NotImplementedError


@scenario('features\checkout_your_information.feature', 'User clicks the Cart button')
def test_user_clicks_the_cart_button():
    """User clicks the Cart button."""
    raise NotImplementedError


@scenario('features\checkout_your_information.feature', 'User fills in the checkout form partially and validates error messages')
def test_user_fills_in_the_checkout_form_partially_and_validates_error_messages():
    """User fills in the checkout form partially and validates error messages."""
    raise NotImplementedError


@scenario('features\checkout_your_information.feature', 'User fills in the checkout form with valid information')
def test_user_fills_in_the_checkout_form_with_valid_information():
    """User fills in the checkout form with valid information."""
    raise NotImplementedError


@scenario('features\checkout_your_information.feature', 'User verifies expected elements on the checkout: Your Information page')
def test_user_verifies_expected_elements_on_the_checkout_your_information_page():
    """User verifies expected elements on the checkout: Your Information page."""
    raise NotImplementedError






@then(parsers.parse ('response should have below attributes:\n{attr_table}'))
def the_following_elements_should_be_visible():
    raise NotImplementedError

