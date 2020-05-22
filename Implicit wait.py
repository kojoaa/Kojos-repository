from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome Driver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title)

time.sleep(10)

assert 'Welcome: Mercury Tours' in driver.title
user_ele=driver.find_element_by_name("userName")
pass_ele=driver.find_element_by_name("password")


user_ele.send_keys("kojo_amissah")
pass_ele.send_keys("Udahawknama1")


driver.find_element_by_name('login').click()