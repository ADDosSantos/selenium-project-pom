from selenium.webdriver.common.by import By
from tests.pages.base_page import BasePage

class ItemPage(BasePage):

        # Locator attributes
    btn_add_to_cart_locator = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    icon_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")
    btn_back_to_products_locator = (By.XPATH, "//button[@id='back-to-products']")

        # Test methods

    def click_btn_add_to_cart(self):
        self.click(self.btn_add_to_cart_locator)

    def click_icon_shopping_cart(self):
        self.click(self.icon_shopping_cart)

    def click_btn_add_to_cart(self):
        self.click(self.btn_back_to_products_locator)