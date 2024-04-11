from pages.base_page import BasePage
from pages.products_page import ProductsPage
from selenium.webdriver.common.by import By
from faker import Faker
import random

class CheckoutPage(BasePage):

    # Locator attributes
    field_first_name_locator = (By.XPATH, "//input[@id='first-name']")
    field_last_name_locator = (By.XPATH, "//input[@id='last-name']")
    field_postal_code_locator = (By.XPATH, "//input[@id='postal-code']")
    btn_continue_locator = (By.XPATH, "//*[@id='continue']")
    checkout_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    checkout_page_title_text = "Checkout: Your Information"
    checkout_page_title_text_overview = "Checkout: Overview"
    checkout_page_title_text_complete = "Checkout: Complete!"
    btn_finish_locator = (By.XPATH, "//button[@id='finish']")
    img_poney_express_ok = (By.XPATH, "//img[@alt='Pony Express' and @class='pony_express']")
    txt_thank_you = (By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']")
    txt_order_dispatched = (By.XPATH, "//*[@class='complete-text' and text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']")
    btn_back_home = (By.XPATH, "//button[@id='back-to-products' and text()='Back Home']")

### ASSERTing Page has correct title and Expected elements both in checkout overview. Finnishing purchase.

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
    def fill_in_checkout_form_continue(self):
        self.write(self.field_first_name_locator,  self.keys_first_name)
        self.write(self.field_last_name_locator, self.keys_last_name)
        self.write(self.field_postal_code_locator, self.postal_code)
        self.click(self.btn_continue_locator)

    def click_btn_finish(self):
        self.assert_element_displayed(self.btn_finish_locator)
        self.click(self.btn_finish_locator)

    # Assertion methods

    def assert_checkout_page_title(self): 
        self.assert_page_title(self.checkout_page_title_locator, self.checkout_page_title_text)

    def assert_checkout_overview_products(self, products):
        product_page = ProductsPage(self.browser)
        for product in products:
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
