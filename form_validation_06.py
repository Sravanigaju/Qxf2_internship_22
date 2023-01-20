"""
Check for the presence of absence of page elements
DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2
AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com
SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Check for the validation message
5) Close the browser
"""
import time
from selenium import webdriver
# Create an instance of IE WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://www.w3.org/WAI/tutorials/forms/validation/")
# Find the click me! button and click it
button  = driver.find_element("xpath" ,"//form[@id='valform']//div//div//input[@value='Submit']")
button.click()
# Pause the script to wait for validation messages to load
time.sleep(3)
# KEY POINT: Check if the validation mesage for email field
try:
    driver.find_element("xpath", "//input[@id='email']")
except RuntimeError as e: #
 #This pattern of catching all exceptions is ok when you are starting out
    RESULT_FLAG = False #
else:
    RESULT_FLAG = True
if RESULT_FLAG is True:
    print("Validation message for name present")
else:
    print("Validation message for name NOT present")
# Close the browser window
driver.close()
