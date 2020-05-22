from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #allows the use of timers

driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe')#opens browser

driver.get(=)#opens url

print(driver.title)#gets the title
time.sleep(5)#sets timer

driver.get('http://www.pavantestingtools.com/')

print(driver.title)
time.sleep(5)

driver.back()

print(driver.title)
time.sleep(5)

driver.forward()

print(driver.title)
time.sleep(5)