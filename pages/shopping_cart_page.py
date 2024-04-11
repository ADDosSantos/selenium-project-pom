from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

        # Locator attributes
        
        backpack_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']")
        onesie_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Onesie']")
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

        def assert_Backpack_displayed(self):
            self.assert_element_displayed(self.backpack_locator)

        def assert_onesie_displayed(self):
            self.assert_element_displayed(self.onesie_locator)
        
        def assert_cart_page_title(self):
            self.assert_page_title(self.cart_page_title_locator, self.cart_page_title_text)

        def element_not_present(self):
            self.assert_element_NOT_displayed(self.cart_page_title_locator)


                
