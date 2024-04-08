import pytest
import time
import requests
import os
from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.support.select import Select

# Configuring Selenoid
base_url = "http://localhost"
selenoid_url = f"{base_url}:4444/wd/hub"
videos_url = f"{base_url}:4444/video/"

# Create the project folder for videos if it doesn't exist
videos_folder = "videos"
if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)


@pytest.fixture(scope="function")
def browser():
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
    driver.get("https://www.saucedemo.com")
    driver.set_window_size(1280, 1024)
    
    # initializing explicit and implicit waits
    wait = WebDriverWait(driver, 30)
    driver.implicitly_wait(7) 
    
    yield driver
    # Begin Teardown
    session_id = driver.session_id
    print (f"Session ID: {session_id}")
    driver.quit()
    download_video(session_id, videos_folder)



def download_video(session_id, videos_folder):
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
