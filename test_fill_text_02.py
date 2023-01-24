"""Learn to fill text fields 
"""
import time
from selenium import webdriver
# Create an instance of Firefox WebDriver
def test_title():
    driver = webdriver.Firefox()
# The driver.get method will navigate to a page given by the URL
    driver.get("https://qxf2.com/selenium-tutorial-main")
# Find the name field using xpath with id
    name =  driver.find_element("xpath", "//input[@id='name']")
# KEY POINT: Send text to an element using send_keys method
    name.send_keys('sravani')
# Find the email field using xpath without id
    email = driver.find_element("xpath", "//input[@name='email']")
    email.send_keys('sravanigajula99@gmail.com')
# Find the phone no field using id
    phone = driver.find_element("id", "phone")
    phone.send_keys('12355666679')
# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
    time.sleep(3)
# Close the browser window
    driver.close()
