import time

from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.item_page import ItemPage
from pages.shopping_cart_page import CartPage
from pages.checkout_page import CheckoutPage

class Test_02_add_products_to_cart():
    
    username = "standard_user"
    password = "secret_sauce"

    def test_02_add_products_to_cart(self, browser: WebDriver):
        time.sleep(3) # for demo purposes
        # user logs in
        login_page = LoginPage(browser)
        time.sleep(3) # Demo purposes only.
        login_page.perform_login(self.username, self.password)
        products_page = ProductsPage(browser)
        products_page.assert_products_page_title()
        # Adding Backpack to cart
        products_page.find_and_enter_item_page("Sauce Labs Backpack")
        item_page = ItemPage(browser)
        item_page.click_btn_add_to_cart()
        # ASSERTing Backpack in cart
        item_page.click_btn_view_shopping_cart()
        shopping_cart_page = CartPage(browser)
        shopping_cart_page.assert_cart_page_title()
        shopping_cart_page.assert_item_displayed("Sauce Labs Backpack")
        # Adding Onesie as item
        shopping_cart_page.click_continue_shopping()
        products_page.find_and_enter_item_page("Sauce Labs Onesie")
        item_page.click_btn_add_to_cart()
        # ASSERTing Onesie in cart
        item_page.click_btn_view_shopping_cart()
        shopping_cart_page.assert_cart_page_title()
        shopping_cart_page.assert_item_displayed("Sauce Labs Onesie")
        # proceed to checkout
        shopping_cart_page.click_checkout()
        checkout_page = CheckoutPage(browser)
        checkout_page.assert_checkout_page_title()
        checkout_page.fill_in_checkout_form_continue()
        checkout_page.assert_checkout_overview_products(("Sauce Labs Onesie", "Sauce Labs Backpack"))
        checkout_page.assert_checkout_overview_page_title()
        checkout_page.click_btn_finish()
        checkout_page.assert_checkout_complete_elements()
