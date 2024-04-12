from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locator attributes
    form_username_locator = (By.ID, "user-name")
    form_password_locator = (By.ID, "password")
    btn_login_locator = (By.ID, "login-button")
    login_error_message_locator = (By.XPATH, "//*[@data-test = 'error']")
    expected_text = "Username and password do not match any user in this service"
    login_logo_locator = (By.XPATH, "//div[@class = 'login_logo']")

    # Test methods
    def open(self):
        self.navigate_to("https://www.saucedemo.com")

    def perform_login(self, username, password):
        self.write(self.form_username_locator, username)
        self.write(self.form_password_locator, password)
        
    def click_login_button(self): 
        self.click(self.btn_login_locator)

    # Assertion methods

    def assert_bad_login_error_exists(self):
        self.assert_element_displayed(self.login_error_message_locator)

    def assert_bad_login_error_message(self):
        captured_text = self.capture_element_text(self.login_error_message_locator)
        print(f"\n\n{captured_text}\n\n")
        assert self.expected_text in captured_text, "\nCaptured text {captured_text} does not match expected text: {expected_text}. (Contained)"

    def is_on_login_page(self):
        self.assert_element_displayed(self.login_logo_locator)
        self.assert_element_displayed(self.btn_login_locator)
