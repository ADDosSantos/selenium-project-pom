from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ItemPage(BasePage):

        # Locator attributes
    btn_add_to_cart_locator = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    icon_shopping_cart = (By.XPATH, "//a[@class='shopping_cart_link']")

        # Test methods

    def click_btn_add_to_cart(self):
        self.click(self.btn_add_to_cart_locator)

    def click_icon_shopping_cart(self):
        self.click(self.icon_shopping_cart)
