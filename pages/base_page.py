
class BasePage:
    def __init__(self, browser):
        self.browser = browser

    # Generic testing methods

    def find_element(self, locator):
        return self.browser.find_element(*locator)
    
    def find_elements(self, locator):
        return self.browser.find_elements(*locator)
    
    def write(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()


    # Generic testing methods

    def assert_element_displayed(self, locator):
        assert self.browser.find_element(*locator).is_displayed()