import time
import os

## Get the directory of the current script
#current_directory = os.path.dirname(os.path.realpath(__file__))
#
## Navigate up one level to reach the project directory
#project_directory = os.path.dirname(current_directory)
#
## Add the project directory to the Python path
#import sys
#sys.path.append(project_directory)

# Now you have the project directory available for importing modules
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class Test_01_Login_Valid():

    username = "standard_user"
    password = "secret_sauce"

    def test_01_login_valido(self, browser):
            time.sleep(3) # for demo purposes
            login_page = LoginPage(browser)
            login_page.perform_login(self.username, self.password)
            landing_page = ProductsPage(browser)
            landing_page.assert_products_page_title()






