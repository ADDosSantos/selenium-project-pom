import pytest
import time
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait

# Configuring Selenoid
base_url = "http://localhost"
selenoid_url = f"{base_url}:4444/wd/hub"
videos_url = f"{base_url}:4444/video/"

# Create the project folder for videos if it doesn't exist
videos_folder = "videos"
if not os.path.exists(videos_folder):
    os.makedirs(videos_folder)

def pytest_addoption(parser):
    parser.addoption("--remote", action="store_true", help="Run tests remotely using Selenoid")
    parser.addoption("--headless", action="store_true", help="Specify headless execution for testing")
    parser.addoption("--browser", action="store", default="chrome", help="Specify the browser for testing")
    
@pytest.fixture(scope="class")
def browser(request):
    # Check if --local parameter is passed
    use_remote = request.config.getoption("--remote")
    # Check if --browser parameter is passed
    browser_type = request.config.getoption("--browser")
    # Check if --browser parameter is passed
    headless = request.config.getoption("--headless")

        # Define desired capabilities
    capabilities = {
        "chrome": DesiredCapabilities.CHROME.copy(),
        "firefox": DesiredCapabilities.FIREFOX.copy(),
    }
    options = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
    }

    if use_remote:
        # Set Selenoid options for video recording
        selenoid_options = {"enableVideo": True}
        if headless and browser_type.lowercase()=="chrome":
            selenoid_options.update({"headless": True})
        if headless and browser_type.lowercase()=="firefox":
            selenoid_options.update({"moz:headless": True})

        options[browser_type].set_capability("selenoid:options", selenoid_options)
        driver = webdriver.Remote(selenoid_url, desired_capabilities=capabilities[browser_type], options=options[browser_type]) ###SERVER DOWN!!!
    
    if not use_remote:
        # Define options for Chrome and Firefox
        options = {
            "chrome": ChromeOptions(),
            "firefox": FirefoxOptions(),
        }

        # I was having fun... why not?
        if headless:
            options[browser_type].add_argument("--headless")

        if browser_type == "chrome":
            # Set any desired capabilities for Chrome
            options[browser_type].add_argument("--window-size=1280,1024")  # Example of adding a Chrome option
            # Initialize local Chrome WebDriver with options
            driver = webdriver.Chrome(options=options[browser_type])
        elif browser_type == "firefox":
            # Set any desired capabilities for Firefox
            options[browser_type].add_argument("--width=1280")
            options[browser_type].add_argument("--height=1024")
    
            # Initialize local Firefox WebDriver with options
            driver = webdriver.Firefox(options=options[browser_type])
        else:
            raise ValueError("Invalid browser type specified.")

    # Initializing implicit wait
    driver.implicitly_wait(7) 
    session_id = driver.session_id
    driver.get("https://www.saucedemo.com")

    yield driver

    # Begin Teardown
    print(session_id)
    driver.quit()
    if use_remote:
        download_video(session_id)

@pytest.fixture
def explicit_wait(driver):
    wait = WebDriverWait(driver, 30)
    yield wait

def download_video(session_id):
    # As per Selenoid documentation, target of the video.
    video_url = f"{videos_url}{session_id}.mp4"
    # Define the file path for saving the video file
    file_path = os.path.join(videos_folder, f"{session_id}.mp4")
    
    # Download the video file
    # Note: Selenoid has an small (known) issue: it takes some time to process and make the videos available 
    # Sometimes the download request is faster, causing an error. So, a retry mechanism is necessary. 
    # Sorry for the time.sleep.
    
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
