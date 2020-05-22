from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\Chrome Driver\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")

links=driver.find_elements(By.TAG_NAME, "a")

print("number of links present",len(links))

for link in links:
    print(link.text)

driver.find_element_by_link_text("REGISTER").click()
