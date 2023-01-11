from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
email=driver.find_element("xpath","//input[@id='email']")
email.send_keys("sravanigajula99@gmail.com")
password=driver.find_element("xpath","//input[@placeholder='Password']")
password.send_keys("12345")
login=driver.find_element("xpath","//button[@type='submit']")
login.click()

