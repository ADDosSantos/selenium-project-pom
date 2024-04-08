from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
        # Test methods

        def __init__(self, browser):
            self.browser = browser
        
        # Locator attributes
            self.form_username_locator = (By.ID, "user-name")
            self.form_password_locator = (By.ID, "password")
            self.btn_login_locator = (By.ID, "login-button")
            self.login_error_message_locator = (By.XPATH, "//*[@data-test = 'error' and contains(text(), 'Username and password do not match any user in this service' )]")
            self.login_logo_locator = (By.XPATH, "//div[@class = 'login_logo']")

        # Test methods
        def perform_login(self, username, password):
            self.write(self.form_username_locator, username)
            self.write(self.form_password_locator, password)
            self.click(self.btn_login_locator)
            #self.browser.find_element(*self.form_username_locator).send_keys(username)
            #self.browser.find_element(*self.form_password_locator).send_keys(password)
            #self.browser.find_element(*self.btn_login_locator).click()
        
        # Assertion methods

        def assert_bad_login(self):
            self.assert_element_displayed(self.login_error_message_locator)
            # assert self.browser.find_element(*self.login_error_message_locator).is_displayed()

        def assert_login_logo(self):
            self.assert_element_displayed(self.login_logo_locator)
            # assert self.browser.find_element(*self.login_logo_locator).is_displayed()

