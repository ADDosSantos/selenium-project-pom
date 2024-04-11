from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):
        
        def __init__(self, driver):
            super().__init__(driver)
        
        # Locator attributes

        item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")
        #backpack_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']")
        #onesie_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Onesie']")
        btn_go_to_cart_locator = (By.XPATH, "//a[@class, 'shopping_cart_link')]")
        products_page_title_locator = (By.XPATH, "//span[@class = 'title']")
        products_page_title_text = "Products"

        # Test methods

        def find_and_enter_item_page(self, item_name):
            item_locator = (self.item_locator[0], self.item_locator[1].format(item_name))
            self.assert_element_displayed(item_locator)
            self.click(self.item_locator)

        #def find_and_enter_backpack_item_page(self):
        #    self.assert_element_displayed(self.backpack_locator)
        #    self.click(self.backpack_locator)
        #
        #def find_and_enter_onesie_item_page(self):
        #    self.assert_element_displayed(self.onesie_locator)
        #    self.click(self.onesie_locator)

        def click_btn_go_to_cart(self):
            self.assert_element_displayed(self.btn_go_to_cart_locator)
            self.click(self.btn_go_to_cart_locator)

        def assert_products_page_title(self):
            self.assert_page_title(self.products_page_title_locator, self.products_page_title_text)



                
