import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locator attributes
    form_username_locator = (By.ID, "user-name")
    form_password_locator = (By.ID, "password")
    btn_login_locator = (By.ID, "login-button")
    login_error_message_locator = (By.XPATH, "//*[@data-test = 'error']")
    login_logo_locator = (By.XPATH, "//div[@class = 'login_logo']")

    # Test methods
    def open(self, headless):
        if not headless:
            time.sleep(2) # for demo purposes.
        self.navigate_to("https://www.saucedemo.com")

    def open_cart(self):
        self.navigate_to("https://www.saucedemo.com/cart")

    def perform_login(self, username, password):
        self.write(self.form_username_locator, username)
        self.write(self.form_password_locator, password)
        
    def click_login_button(self): 
        self.click(self.btn_login_locator)

    # Assertion methods

    def assert_bad_login_error_exists(self):
        self.assert_element_displayed(self.login_error_message_locator)

    def assert_bad_login_error_message(self, error_message):
        captured_text = self.capture_element_text(self.login_error_message_locator)
        print(f"\n\n{captured_text}\n\n")
        assert error_message in captured_text, f"\nCaptured text {captured_text} does not match expected text: {error_message}. (Contained)"

    def is_on_login_page(self):
        self.assert_element_displayed(self.login_logo_locator)
        self.assert_element_displayed(self.btn_login_locator)

    def validate_presence_login_page_elements(self, attr_table):
        locators = {
            "Page title": "login_logo_locator",
            "Username form": "form_username_locator",
            "Password form": "form_password_locator",
            "Login button": "btn_login_locator",
            "Login credentials": "your_login_credentials_locator",
            "Passwords": "your_passwords_locator"
        }
        for row in attr_table:
            for element_name in row:
                locator = locators.get(element_name)
                if locator:
                    assert self.assert_element_displayed(locator), f"Element '{locator}' is not visible"
