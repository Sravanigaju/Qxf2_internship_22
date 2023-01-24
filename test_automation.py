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
def test_automation(self):
    driver=webdriver.Chrome()
# KEY POINT: The driver.get method will navigate to a page given by the URL
    driver.get("https://mlac.edmis.in/")
    #enter registernumber
    registernumber= driver.find_element("xpath","//input[@id='RegisterNumber']")
    registernumber.send_keys("19mlacv2003")
    #enter date of birth
    dob=driver.find_element("xpath","//input[@id='DOB']")
    dob.send_keys("17-06-2001")
    #enter your email id
    email=driver.find_element("xpath","//input[@id='Email_ID']")
    email.send_keys("******@com")
    #enter the phone number
    phoneno= driver.find_element("xpath","//input[@id='Phone_No']")
    phoneno.send_keys("**********")
    #click on login button
    login=driver.find_element("xpath","//button[@id='BtnStudentLogin']")
    login.click()
