from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ItemPage(BasePage):
        
    def __init__(self, browser):
        super().__init__(browser)
        
        # Locator attributes
    btn_add_to_cart_locator = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    btn_to_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")

        # Test methods

    def click_btn_add_to_cart(self):
        self.click(self.btn_add_to_cart_locator)
    def click_btn_add_to_cart(self):
        self.click(self.btn_add_to_cart_locator)
    def click_btn_view_shopping_cart(self):
        self.click(self.btn_to_shopping_cart)

  
        # Assertion methods
        
#        def assert_page_title(self):
#            self.assert_element_displayed(self.products_page_title_locator)
#
#        def element_not_present(self):
#            self.assert_element_NOT_displayed(self.products_page_title_locator)
