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
# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://www.amazon.in/")
# Locate the Menu icon and click on it
home = driver.find_element("xpath", "//i[@class='hm-icon nav-sprite']")
home.click()
# Locate the Resource element to hover over
Trending = driver.find_element("xpath", "//div[normalize-space()='trending']")
# KEY POINT: Use ActionChains to hover over elements
action = ActionChains(driver)
action.move_to_element(Trending)
action.perform()
time.sleep(2) #Adding waits to make the example more visual
# Click the GUI automation link
cart = driver.find_element("x-path","//span[@id='nav-cart-count']" )
cart.click()
# Wait for 3 seconds for the page to load
time.sleep(3)
# Close the browser
driver.close()
