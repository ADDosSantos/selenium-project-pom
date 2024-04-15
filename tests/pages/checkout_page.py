from tests.pages.base_page import BasePage
from tests.pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from faker import Faker
import random
import time

class CheckoutPage(BasePage):

    # Locator attributes
    field_first_name_locator = (By.XPATH, "//input[@id='first-name']")
    field_last_name_locator = (By.XPATH, "//input[@id='last-name']")
    field_postal_code_locator = (By.XPATH, "//input[@id='postal-code']")
    btn_continue_locator = (By.XPATH, "//*[@id='continue']")
    btn_cancel_locator = (By.XPATH, "//*[@id='cancel']")
    checkout_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    checkout_page_title_text = "Checkout: Your Information"
    checkout_page_title_text_overview = "Checkout: Overview"
    checkout_page_title_text_complete = "Checkout: Complete!"
    btn_finish_locator = (By.XPATH, "//button[@id='finish']")
    img_poney_express_ok = (By.XPATH, "//img[@alt='Pony Express' and @class='pony_express']")
    txt_thank_you = (By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']")
    txt_order_dispatched = (By.XPATH, "//*[@class='complete-text' and text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']")
    btn_back_home = (By.XPATH, "//button[@id='back-to-products' and text()='Back Home']")
    error_message_locator = (By.XPATH, "//div[@class='error-message-container error']")
    icon_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        # passing faker as fixture in method definition
        seed_int = random.randint(1, 999999999)
        Faker.seed(seed_int)
        faker = Faker()
        self.keys_first_name = faker.first_name()
        self.keys_last_name = faker.last_name()
        self.postal_code = faker.postalcode_in_state('AK') # Alaska
        
    # Test methods
    def fill_in_checkout_form_continue(self, first_name = None, last_name = None, postal_code = None):
        # If I pass arguments, it will validate the first part of the or as true, and assume the passed argument
        # if I do not pass an argument, it will generate using faker
        # if the argument is the string "empty", it will assume empty string

        first_name = "" if first_name == "empty" else first_name or self.first_name
        last_name = "" if last_name == "empty" else last_name or self.last_name
        postal_code = "" if postal_code == "empty" else postal_code or self.postal_code

        self.write(self.field_first_name_locator,  first_name)
        self.write(self.field_last_name_locator, last_name)
        self.write(self.field_postal_code_locator, postal_code)
        time.sleep(1)
        self.click(self.btn_continue_locator)

    def click_btn_finish(self):
        self.assert_element_displayed(self.btn_finish_locator)
        self.click(self.btn_finish_locator)

    def click_btn_cancel(self):
        self.assert_element_displayed(self.btn_cancel_locator)
        self.click(self.btn_cancel_locator)

    def click_icon_cart(self):
        self.assert_element_displayed(self.icon_shopping_cart)
        self.click(self.icon_shopping_cart)
        

    # Assertion methods

    def validate_presence_checkout_information_page_elements(self, attr_table):
        locators = {
            "first name field": "field_first_name_locator",
            "last name field": "field_last_name_locator",
            "zip code field": "field_postal_code_locator",
            "continue button": "btn_continue_locator",
            "cancel button": "btn_cancel_locator"
        }
        self.assert_list_of_locators(locators, attr_table)

    def fill_in_checkout_form(self, attr_table):
        locators = {
            "First Name": "field_first_name_locator",
            "Last Name": "field_last_name_locator",
            "Zip/Postal Code": "field_postal_code_locator",
        }
        locator_input_matches = self.form_filler_multiple_fields_friendly_matcher(locators, attr_table)
        print("..................... data_dict as locator_input_matches")
        print(locator_input_matches)
        for key, value in locator_input_matches.items():
            # this could be more syntetic, but easier to read this way.
            attribute_name = key
            print("..................... attribute_name")
            print(attribute_name)
            locator = getattr(self, attribute_name, None)
            self.driver.find_element(*locator).send_keys(value)
        

    def click_continue_checkout(self):
        self.click(self.btn_continue_locator)

        

    def assert_checkout_page_title(self): 
        self.assert_page_title(self.checkout_page_title_locator, self.checkout_page_title_text)

    def assert_checkout_overview_products(self, *products):
        product_page = ProductsPage(self.browser)
        product_tuple = products
        for product in product_tuple:
            item_locator = (product_page.item_locator[0], product_page.item_locator[1].format(product))
            self.assert_element_displayed(item_locator)

    def assert_checkout_overview_page_title(self):
        self.assert_page_title(self.checkout_page_title_locator, self.checkout_page_title_text_overview)

    def assert_checkout_complete_elements(self):
        self.assert_page_title(self.checkout_page_title_locator, self.checkout_page_title_text_complete)
        self.assert_element_displayed(self.img_poney_express_ok)
        self.assert_element_displayed(self.txt_thank_you)
        self.assert_element_displayed(self.txt_order_dispatched)
        self.assert_element_displayed(self.btn_back_home)

    def validate_error_message_as_expected(self, error_message):
        self.assert_element_displayed(self.error_message_locator)
        captured_text = self.capture_element_text(self.error_message_locator)
        print(f"\n\n{captured_text}\n\n")
        assert error_message in captured_text, f"\nCaptured text {captured_text} does not match expected text: {error_message}. (Contained)"
