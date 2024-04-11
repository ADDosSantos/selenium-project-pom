from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locator attributes
    form_username_locator = (By.ID, "user-name")
    form_password_locator = (By.ID, "password")
    btn_login_locator = (By.ID, "login-button")
    login_error_message_locator = (By.XPATH, "//*[@data-test = 'error' and contains(text(), 'Username and password do not match any user in this service' )]")
    login_logo_locator = (By.XPATH, "//div[@class = 'login_logo']")

    # Test methods
    def perform_login(self, username, password):
        self.write(self.form_username_locator, username)
        self.write(self.form_password_locator, password)
        self.click(self.btn_login_locator)

    # Assertion methods

    def assert_bad_login_error_exists(self):
        self.assert_element_displayed(self.login_error_message_locator)

    def assert_bad_login_error_message(self, expected_text):
        captured_text = self.capture_element_text(self.login_error_message_locator)
        assert captured_text == expected_text

    def assert_login_logo(self):
        self.assert_element_displayed(self.login_logo_locator)
