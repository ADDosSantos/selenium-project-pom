from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class CartPage(BasePage):

    # Locator attributes

    item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")
    btn_continue_shopping_locator = (By.XPATH, "//button[@id='continue-shopping']")
    cart_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    cart_page_title_text = "Your Cart"
    btn_checkout = (By.XPATH, "//button[@id='checkout']")

    # Test methods
    def click_continue_shopping(self):
        self.click(self.btn_continue_shopping_locator)

    def click_checkout(self):
        self.click(self.btn_checkout)
    # Assertion methods
    def assert_item_displayed(self, item_name):
        item = (self.item_locator[0], self.item_locator[1].format(item_name))
        self.assert_element_displayed(item)

    def assert_cart_page_title(self):
        self.assert_page_title(self.cart_page_title_locator, self.cart_page_title_text)

    def validate_presence_of_selected_items(self, shopping_list):
        for item in shopping_list.keys():
            self.assert_item_displayed(item)