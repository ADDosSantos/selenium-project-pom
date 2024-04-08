import time
import pytest
from pages.login_page import LoginPage
from pages.products_page_landing import ProductsPage


username = "standard_user"
password = "secret_sauce"
bad_username = "zzzzzzzzzzzz"

def test_01_login_valido(browser):
        login_page = LoginPage(browser)
        time.sleep(3) # Demo purposes only.
        login_page.perform_login(bad_username, password)
        landing_page = ProductsPage(browser)
        landing_page.assert_page_title()
        time.sleep(3) # Demo purposes only.

def test_02_login_invalido(browser):
        login_page = LoginPage(browser)
        time.sleep(5) # Demo purposes only.
        login_page.perform_login(bad_username, password)
        time.sleep(3) # Demo purposes only.
        login_page.assert_bad_login()
        login_page.assert_login_logo()





