from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    # Locator attributes
    item_locator = (By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='{}']")
    btn_go_to_cart_locator = (By.XPATH, "//a[@class, 'shopping_cart_link')]")
    products_page_title_locator = (By.XPATH, "//span[@class = 'title']")
    products_page_title_text = "Products"

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
