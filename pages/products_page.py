from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import random
import pytest

class ProductsPage(BasePage):

    # Locator attributes
    item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")
    btn_go_to_cart_locator = (By.XPATH, "//a[@class, 'shopping_cart_link')]")
    products_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    products_page_title_text = "Products"
    icon_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    general_item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name')]")
    item_relative_add_to_cart_btn = (By.XPATH, "/../../following-sibling::div/button[text()='Add to cart']")
    item_relative_price_info = (By.XPATH, "/../../following-sibling::div/*[@class='inventory_item_price']")

    # e.g. (//*[contains(@class, 'inventory_item_name')])[1]/../../following-sibling::div/*[@class='inventory_item_price']

    # Test methods
    def find_and_enter_item_page(self, item_name):
        item_locator = (self.item_locator[0], self.item_locator[1].format(item_name))
        self.assert_element_displayed(item_locator)
        self.click(item_locator)

    def click_btn_go_to_cart(self):
        self.assert_element_displayed(self.btn_go_to_cart_locator)
        self.click(self.btn_go_to_cart_locator)

    def assert_products_page_title(self):
        self.assert_page_title(self.products_page_title_locator, self.products_page_title_text)

    def add_random_nr_items_to_cart(self):
        # Finds all items in products and adds a random number in random positions to the cart.
        # ALSO stores its name and price in a dict and stores in context
        all_items = self.find_elements(self.general_item_locator)
        total_item_count = len(all_items)
        nr_items_to_add = random.randint(1, total_item_count)
        selected_prod_indices = set()
        shopping_list = {}
        
        while len(selected_prod_indices) < nr_items_to_add:

            random_index = random.randint(0, total_item_count - 1)
            
            # Check if the index is not already selected, so we don't 
            # try to select the same product twice (add button gone)
            if random_index not in selected_prod_indices:
                # Mark the index as selected
                selected_prod_indices.add(random_index)

                # Get the item at the index
                item = all_items[random_index]

                # Click "Add to Cart" button for the selected item
                item_add_to_cart_btn = item.find_element(self.item_relative_add_to_cart_btn)
                self.click(item_add_to_cart_btn)
                
                # Get item name and price
                item_name = item.text
                item_price = item.find_element(self.item_relative_price_info).text
                
                # Add this to shopping_list
                shopping_list[item_name] = item_price
    
        # Store shopping list in the pytest request context :-)
        pytest.request.context.shopping_list = shopping_list
    
    def click_icon_shopping_cart(self):
        self.click(self.icon_shopping_cart)
