from selenium.webdriver.common.by import By

class ProductsPage():
        
        # Locator attributes
        
        products_page_title_locator = (By.XPATH, "//span[@class = 'title']")

        def __init__(self, browser):
            self.browser = browser

        # Test methods
        
        # Assertion methods
        def assert_page_title(self):
            assert self.browser.find_element(*self.products_page_title_locator).is_displayed()

        def element_not_present(self):
            assert self.browser.find_elements(*self.products_page_title_locator) < 0

                
