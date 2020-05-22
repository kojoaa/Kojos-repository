from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome Driver\chromedriver.exe")

driver.get('https://www.expedia.com/')
print(driver.title)

driver.find_element_by_id("tab-flight-tab-hp").click()
driver.find_element_by_id("flight-type-roundtrip-label-hp-flight").click()
driver.find_element_by_id("flight-origin-hp-flight").send_keys("NYC")
driver.find_element_by_id("flight-destination-hp-flight").send_keys("Lagos")