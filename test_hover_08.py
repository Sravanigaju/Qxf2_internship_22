"""
Learn to hover over elements using Selenium
DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2
AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com
SCOPE:
1) Launch Firefox driver
2) Navigate to Qxf2 Tutorial page
3) Click on Menu icon
4) Hover over Resource and GUI automation and click on GUI automation link
5) Close the browser
"""
import time
from selenium import webdriver
#Notice this extra import statement!
from selenium.webdriver.common.action_chains import ActionChains
def test_hover():
# Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()
# Navigate to  page
    driver.get("https://www.w3schools.com/")
# Locate the Menu icon and click on it
    exercises = driver.find_element("xpath", "//a[@id='navbtn_exercises']")
    exercises.click()
# Locate the Resource element to hover over
    cssexercises  = driver.find_element("xpath", "//a[normalize-space()='CSS Exercises']")
# KEY POINT: Use ActionChains to hover over elements
    action = ActionChains(driver)
    action.move_to_element(cssexercises)
    action.perform()
    time.sleep(2) #Adding waits to make the example more visual
    # Click the GUI automation link
    startcssexercises = driver.find_element("x-path","//a[contains(text(),'Start CSS Exercises ❯')]" )
    startcssexercises.click()
# Wait for 3 seconds for the page to load
    time.sleep(3)
# Close the browser
    driver.close()
