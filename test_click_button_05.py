"""
Learn to click a button with Selenium
"""
import time
from selenium import webdriver
def test_click_button():
# Create an instance of Chrome WebDriver
    driver = webdriver.Chrome()
# Maximize the browser window
    driver.maximize_window()
# Navigate to Qxf2 Tutorial page
    driver.get("https://www.w3schools.com/css/default.asp")
# KEY POINT: Locate the button and click on it
    button  = driver.find_element("xpath", "//button[normalize-space()='Submit Answer »']")
    button.click()
# Pause the script to wait for page elements to load
    time.sleep(3)
# Close the browser
    driver.close()
