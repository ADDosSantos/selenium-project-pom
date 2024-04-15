from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage
import random

class ProductsPage(BasePage):

    # Locator attributes
    item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")
    btn_go_to_cart_locator = (By.XPATH, "//a[@class, 'shopping_cart_link')]")
    products_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    products_page_title_text = "Products"
    icon_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    general_item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name')]")
    item_relative_add_to_cart_btn_xpath = "/../../following-sibling::div/button[text()='Add to cart']"
    item_relative_price_info_xpath = "/../../following-sibling::div/*[@class='inventory_item_price']"

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

    def add_random_nr_items_to_cart(self, shopping_list):
        # Finds all items in products and adds a random number in random positions to the cart.
        all_items = self.find_elements(self.general_item_locator)

        total_item_count = len(all_items)
        nr_items_to_add = random.randint(1, total_item_count)
        selected_prod_indices = set()
        
        while len(selected_prod_indices) < nr_items_to_add:

            random_index = random.randint(1, total_item_count)
            # (note: this will enter an xpath selector, so first index is 1, not 0)
            # so, all_items[0], but ((By.XPATH, locator)[1])
            
            # Check if the index is not already selected, so we don't 
            # try to select the same product twice (add button gone)
            if random_index not in selected_prod_indices:
                # Mark the index as selected
                selected_prod_indices.add(random_index)
                # Get the item at the index 
                # PS: here is the list of returned elements, we use the random index - 1 (first is 0)
                item = all_items[random_index-1]
                # Click the Button "Add to Cart" for the chosen item
                # This item's button, the xpath of the "parent item" concatenated with 
                # the additional xpath to retrieve the button child element.
                # PS: here is the xpath, we use the random index (as is. vide supra)
                specific_item_xpath = "(" + (self.general_item_locator[1])+")["+ str(random_index) +"]"
                item_add_to_cart_btn_xpath = specific_item_xpath + self.item_relative_add_to_cart_btn_xpath
                self.click((By.XPATH, item_add_to_cart_btn_xpath))
                # Get item name and price
                item_name = item.text
                item_price_locator = specific_item_xpath + self.item_relative_price_info_xpath
                item_price = self.find_element((By.XPATH, item_price_locator)).text                
                # Store the item using the shopping_list fixture :-)
                shopping_list[item_name] = item_price

    def click_icon_shopping_cart(self):
        self.click(self.icon_shopping_cart)
