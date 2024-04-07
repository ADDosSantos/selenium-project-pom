import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import os
from selenium.webdriver.support.select import Select

# Create the project folder if it doesn't exist
videos_folder = "videos"

if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

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

time.sleep(3) # for learning purposes only

### mapping elements

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


assert driver.find_element(By.XPATH, "//span[@class = 'title']").is_displayed()

time.sleep(3) # for learning purposes only



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