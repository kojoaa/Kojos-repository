from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import keyboard as K
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\Chrome Driver\chromedriver.exe")
wait = WebDriverWait(driver, 72)
driver.get("https://e.uat.stanbic.com.gh:8002/RPA/form")
driver.implicitly_wait(12)
print(driver.title)
driver.maximize_window()

element = driver.find_element_by_name("title")
dropdown = Select(element)
dropdown.select_by_visible_text("Mr")

driver.find_element_by_name('mname').send_keys("John Kojo Amissah")
driver.find_element_by_name("sname").send_keys('Adu-Amankwah')
driver.find_element_by_name("dob").send_keys('2nd November 1998')

element = driver.find_element_by_name("gender")
dropdown = Select(element)
dropdown.select_by_visible_text("Male")

element = driver.find_element_by_name("educationLevel")
dropdown = Select(element)
dropdown.select_by_visible_text("Graduate")

driver.find_element_by_xpath('//*[@id="branch-Form"]/div/div[3]/div/div/button[2]/span/span').click()

element = driver.find_element_by_name("nationaility")
dropdown = Select(element)
dropdown.select_by_visible_text("Ghanaian")

element = driver.find_element_by_name("idType")
dropdown = Select(element)
dropdown.select_by_visible_text("Passport")

driver.find_element_by_name("idNo").send_keys('G2492582')

driver.find_element_by_name("idIssue").click()
driver._switch_to.active_element
K.send('tab')
K.send('down')
K.send('tab')
K.send('tab')
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/div/select[1]').click()
time.sleep(2)
K.send('down')
K.send('down')
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td[2]/div').click()
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/button[3]').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/input').click()
driver._switch_to.active_element
K.send('tab')
K.send('down')
K.send('tab')
K.send('tab')
driver.find_element_by_xpath('/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div/select[1]').click()
time.sleep(2)
K.send('down')
K.send('down')
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[6]/div').click()
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/button[3]').click()





# ID Issue


'''driver.find_element_by_name("idExpiration").click()
driver._switch_to.active_element
K.send('tab')
K.send('down')
K.send('tab')
K.send('tab')
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/div/select[1]').click()
time.sleep(2)
K.send('down')
K.send('down')
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td[6]/div').click()
driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/form/div/div[2]/div[4]/div/div/div/div/div/div[2]/div[2]/button[3]').click()'''

'''# Click submit
driver.find_element_by_xpath('/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/div/button[2]/span/span').click()
time.sleep(2)'''

driver.find_element_by_xpath(
    '/html/body/app-root/app-branch-app/div[1]/div/div[2]/div/div/button[2]/span').click()
# confirm Submission
driver.find_element_by_xpath('/html/body/app-root/app-branch-app/div[2]/div/div[2]/div/div[1]/button').click()