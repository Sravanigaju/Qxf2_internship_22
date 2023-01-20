"""
Learn to navigate to a URL using Selenium
SCOPE:
1) Launch Firefox Driver
2) Navigate to Qxf2 Tutorial page
3) Check the page title
4) Close the browser
"""
from selenium import webdriver
# Create an instance of Chrome WebDriver
driver=webdriver.Chrome()
# KEY POINT: The driver.get method will navigate to a page given by the URL
driver.get("https://www.facebook.com/")
email=driver.find_element("xpath","//input[@id='email']")
email.send_keys("sravanigajula99@gmail.com")
password=driver.find_element("xpath","//input[@placeholder='Password']")
password.send_keys("12345")
login=driver.find_element("xpath","//button[@type='submit']")
login.click()
