import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import os
from faker import Faker
from selenium.webdriver.support.select import Select

# Create the project folder if it doesn't exist
videos_folder = "videos"

if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

# Initializing Faker
fake = Faker()
Faker.seed(0)

# Configuring Selenoid
base_url = "http://localhost"
selenoid_url = f"{base_url}:4444/wd/hub"
videos_url = f"{base_url}:4444/video/"

# Define desired capabilities for Chrome browser
chrome_capabilities = DesiredCapabilities.CHROME.copy()
chrome_capabilities["browserName"] = "chrome"

options = ChromeOptions()
selenoid_options = {"enableVideo": True}

options.set_capability("selenoid:options", selenoid_options)

# Initialize WebDriver with Selenoid
driver = webdriver.Remote(
    selenoid_url, options=options
)


# initializing explicit and implicit waits
wait = WebDriverWait(driver, 30)
driver.implicitly_wait(7) 

# starting browser and setting window size 
driver.get("https://www.saucedemo.com")
driver.set_window_size(1280, 1024)



### User performs valid Login

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

### ASSERT valid Login

assert driver.find_element(By.XPATH, "//span[@class = 'title']").is_displayed()

### Adding Backpack to trolley

driver.find_element(By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']").click() # note: website has a but. the class has an extra space. this is a workaround. Would open minor bug.
time.sleep(3) # for learning purposes only

driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart')]").click()


### ASSERTing Backpack in trolley

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

### Returning to Product selection

driver.find_element(By.XPATH, "//button[@id='continue-shopping']").click()

time.sleep(3) # for learning purposes only


### Adding Onesie to trolley (scrolling into view)

bottom_element = driver.find_element(By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Onesie']")
driver.execute_script("arguments[0].scrollIntoView(true);", bottom_element)
bottom_element.click()

driver.find_element(By.XPATH, "//button[contains(@id, 'add-to-cart')]").click()

### ASSERTing Onesie in trolley

driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Onesie']").is_displayed()



### Completing purchase with two items.

driver.find_element(By.XPATH, "//button[@id='checkout']").click()

##### Filling in purchase form

keys_first_name = fake.first_name()
keys_last_name = fake.last_name()
postal_code = fake.postalcode_in_state('AK') # Alaska

driver.find_element(By.XPATH, "//input[@id='first-name']").send_keys(keys_first_name)
driver.find_element(By.XPATH, "//input[@id='last-name']").send_keys(keys_last_name)
driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys(postal_code)

driver.find_element(By.XPATH, "//*[@id='continue']").click()




### ASSERTing Page has correct title and Expected elements both in checkout overview. Finnishing purchase.

assert driver.find_element(By.XPATH, "//span[@class = 'title' and contains(text(), 'Checkout: Overview')]").is_displayed()

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Onesie']").is_displayed()

assert driver.find_element(By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Backpack']").is_displayed()

driver.find_element(By.XPATH, "//button[@id='finish']").click()


### ASSERTing Page checkout has expected elements


assert driver.find_element(By.XPATH, "//span[@class = 'title' and contains(text(), 'Checkout: Complete!')]").is_displayed()

assert driver.find_element(By.XPATH, "//img[@alt='Pony Express' and @class='pony_express']").is_displayed()

assert driver.find_element(By.XPATH, "//*[@class='complete-header' and text()='Thank you for your order!']").is_displayed()
assert driver.find_element(By.XPATH, "//*[@class='complete-text' and text()='Your order has been dispatched, and will arrive just as fast as the pony can get there!']").is_displayed()

assert driver.find_element(By.XPATH, "//button[@id='back-to-products' and text()='Back Home']").is_displayed()


time.sleep(3)

# quit() - good practice

session_id = driver.session_id

# Print or use the session ID as needed
print("Session ID:", session_id)

driver.quit()

# As per Selenoid documentation, target of the video.
video_url = f"{videos_url}{session_id}.mp4"
# Define the file path for saving the video file
file_path = os.path.join(videos_folder, f"{session_id}.mp4")

# Download the video file
for retry in range(4): 
    response = requests.get(video_url, allow_redirects=True)
    time.sleep(retry)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Video file downloaded successfully to {file_path}")
        break
    elif retry == 3:
        print("Failed to download video file")