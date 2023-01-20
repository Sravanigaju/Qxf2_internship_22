"""
Learn to fill and submit a form with Selenium
DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2
AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com
SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Fill all the text field in Example form
4) Click on Click me! button
5) Verify user is taken to Selenium Tutorial redirect page
6) Close the browser
"""
import time
from selenium import webdriver
# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://www.facebook.com/")
#KEY POINT: Code to fill forms
driver.find_element("xpath", "//input[@id='email']").send_keys('sravanigajula99@gmail.com')
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
