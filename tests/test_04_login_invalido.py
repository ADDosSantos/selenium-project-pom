import time
from pages.login_page import LoginPage

class Test_04_Login_Invalid():

    password = "secret_sauce"
    bad_username = "zzzzzzzzzzzz"
    expected_text = "Epic sadface: Username and password do not match any user in this service"
    
    def test_04_login_invalid(self, browser):
            time.sleep(3) # for demo purposes
            login_page = LoginPage(browser)
            login_page.perform_login(self.bad_username, self.password)
            login_page.assert_bad_login_error_exists()
            login_page.assert_bad_login_error_message(self.expected_text)
            login_page.assert_login_logo()