from pytest_bdd import parsers, scenarios, scenario, given, when, then
from tests.pages.login_page import LoginPage
from tests.pages.products_page import ProductsPage

# This assumes that 'features' subfolder is in the same directory as this file
# scenarios('features')

scenarios("../features/login.feature")

# Given steps
@given("the user is on the login page")
def user_is_on_login_page(browser, flag_headless):
    login_page = LoginPage(browser)
    login_page.open(flag_headless)

# When steps
@when("the user enters valid credentials")
def user_enters_valid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.perform_login("standard_user", "secret_sauce")

@when("the user enters valid credentials")
def user_enters_valid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.perform_login("standard_user", "secret_sauce")

@when("the user enters invalid credentials")
def user_enters_invalid_credentials(browser):
    login_page = LoginPage(browser)
    login_page.perform_login("zzzzzzzzzzzz", "secret_sauce")

@when(parsers.parse("the user enters the credentials Username {username} and Password {password}"))
def user_enters_login_credentials(browser, username, password):
    if username == "empty": 
        username = ""
    if password == "empty": 
        password = ""
    login_page = LoginPage(browser)
    login_page.perform_login(username, password)


@when("the user clicks the login button")
def when_user_clicks_login_button(browser):
    login_page = LoginPage(browser)
    login_page.click_login_button()

@then(parsers.parse("the following error message should be present {error_message}"))
def the_following_error_message_should_be_present(browser, error_message):
    login_page = LoginPage(browser)
    login_page.assert_bad_login_error_message(error_message)

# Then steps
@then("the user should be redirected to the products page")
def then_user_redirected_to_products_page(browser):
    products_page = ProductsPage(browser)
    products_page.assert_products_page_title()

@then("the user should remain on the login page")
def then_user_remains_on_login_page(browser):
    login_page = LoginPage(browser)
    login_page.is_on_login_page()

@then("the login logo should be displayed")
def then_login_logo_displayed(browser):
    login_page = LoginPage(browser)
    login_page.assert_login_logo_is_visible()

@then(parsers.parse('the following login page elements should be visible:\n{attr_table}'))
def the_following_elements_should_be_visible(browser, attr_table):
    login_page = LoginPage(browser)
    login_page.validate_presence_login_page_elements(attr_table)
