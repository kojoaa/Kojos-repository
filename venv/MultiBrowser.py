from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox(executable_path='C:\Drivers\geckodriver.exe')
#driver=webdriver.Ie(executable_path='C:\Drivers\IEDriverServer.exe')

driver.get('http://newtours.demoaut.com/')

print(driver.title)#returns title of the page
print(driver.current_url)#return url of the page
driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a').click()
#print(driver.page_source)

time.sleep(5)

driver.close()#closes one tab
#driver.quit()   #closes all the windows