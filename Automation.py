from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#Setting up Chrome driver
service = Service("C:\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#opening the page
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

#Test case 1 : When the login is valid
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

if "Logged In Successfully" in driver.page_source:
    print("Test case 1 Passed : Valid login successful")
else:
    print("Test case 1 failed")

driver.back()
time.sleep(2)

#Test case 2 : Login with invalid credentials
driver.find_element(By.ID, "username").send_keys("wrongUser")
driver.find_element(By.ID, "password").send_keys("wrongPass")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

error_msg = driver.find_element(By.ID, "error").text
if "Your username is invalid!" in error_msg:
    print('Test case 2 is Passed: Error message displayed correctly')
else:
    print("Test case 2 failed")

#Test case 3 : Empty username, valid password is entered
driver.find_element(By.ID,"username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

error_msg = driver.find_element(By.ID, "error").text
if "Your username is invalid!" in error_msg:
    print("Test case 3 Passed: Empty username handled correctly")
else:
    print("Test case 3 Failed")
time.sleep(2)

#Test case 4 : Valid username, empty password is entered
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "submit").click()
time.sleep(2)

error_msg = driver.find_element(By.ID, "error").text
if "Your password is invalid!" in error_msg:
    print("Test case 4 Passed: Empty password handled correctly")
else:
    print("Test case 4 Failed")
time.sleep(2)

#Test case 5 : Both username and password is empty
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "password").clear()
driver.find_element(By.ID, "submit").click()
time.sleep(2)

error_msg = driver.find_element(By.ID, "error").text
if "Your username is invalid!" in error_msg:
    print("Test case 5 Passed: Both fields empty handled correctly")
else:
    print("Test case 5 Failed")

driver.quit()