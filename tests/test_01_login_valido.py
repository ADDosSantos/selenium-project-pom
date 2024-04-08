import time
import pytest
#from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options as ChromeOptions
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import requests
#import os
#from selenium.webdriver.support.select import Select


def test_01_login_valido(browser):
        ### mapping elements
        browser.find_element(By.ID, "user-name").send_keys("standard_user")
        browser.find_element(By.ID, "password").send_keys("secret_sauce")
        browser.find_element(By.ID, "login-button").click()
        assert browser.find_element(By.XPATH, "//span[@class = 'title']").is_displayed()
        
        time.sleep(3) # for learning purposes only
