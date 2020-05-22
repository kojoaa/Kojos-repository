from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe')

driver.get("http://newtours.demoaut.com/")

user_ele=driver.find_element_by_name("userName")

print(user_ele.is_displayed())
print(user_ele.is_enabled())

pass_ele=driver.find_element_by_name("password")
print(pass_ele.is_displayed())
print(pass_ele.is_enabled())

user_ele.send_keys("Kojo_aa")
pass_ele.send_keys("babylonboy")

driver.find_element_by_name("login").click()