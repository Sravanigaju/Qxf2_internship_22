"""
Learn to navigate to a URL using Selenium
"""
from selenium import webdriver
def test_title():
# Create an instance of Firefox WebDriver
    browser = webdriver.Firefox()
# KEY POINT: The driver.get method will navigate to a page given by the URL
    browser.get("https://www.zomato.com/")
# Check if the title of the page is proper
# Quit the browser window
    browser.quit()
