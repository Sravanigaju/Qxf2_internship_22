"""
Learn to select a checkbox using Selenium
"""
import time
from selenium import webdriver
def test_checkbox():
# Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()
    driver.get("https://designsystem.digital.gov/components/checkbox/")
# KEY POINT: Locate the checkbox and click on it
    checkbox = driver.find_element("xpath", "//label[@for='check-historical-douglass']")
    checkbox.click()
# Pause the script for 3 sec so you can confirm the check box was selected
    time.sleep(3)
# Close the browser window
    driver.close()
