"""
Learn to fill and submit a form with Selenium
"""
import time
from selenium import webdriver
def test_form_submit():
# Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()
# Navigate to Qxf2 Tutorial page
    driver.get("https://www.facebook.com/")
#KEY POINT: Code to fill forms
    driver.find_element("xpath", "//input[@id='email']").send_keys('xxxx@gmail.com')
# Find the password no field and fill password no
    password = driver.find_element("xpath","//input[@id='pass']")
    password.send_keys('1224')
# Identify the xpath for Click me button and click on it
    login = driver.find_element("xpath", "//button[@type='submit']")
    login.click()
# Wait for the new page to load
    time.sleep(3)
# Verify user is taken to Qxf2 tutorial redirect url
    if driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect':
        print("Success")
    else:
        print("Failure")
    # Close the browser
    driver.close()
