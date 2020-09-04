password = 'shivsharma@123456'
email = "shivsharma7821@gmail.com"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import clipboard
import time
import os

repository = input("Enter repository Name: ")

driver = webdriver.Chrome('C:\\Users\\Shivam sharma\\Documents\\New\\PythonAutomation\\chromedriver.exe')
driver.get('https://github.com/login')

user = driver.find_element_by_id('login_field')
user.send_keys(email)

user = driver.find_element_by_id('password')
user.send_keys(password)

sign = driver.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]')
sign.submit()

time.sleep(2)

new = driver.find_element_by_xpath('/html/body/div[4]/div/aside/div[2]/div[1]/div/h2/a')
new.click()

time.sleep(4)

new = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input')
new.send_keys(repository)

check = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/div[4]/div[1]/label/input[2]')
check.click()

create = driver.find_element_by_xpath('/html/body/div[4]/main/div/form/div[4]/button')
create.submit()

time.sleep(4)

clone = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/summary')
clone.click()

copy = driver.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/div[1]/div/div/clipboard-copy')
copy.click()

git_url = clipboard.paste()
print(git_url)

os.system('git init')
os.system('git add .')
os.system('git commit -m "Initial commit"')
os.system('git remote add origin '+git_url)
os.system('git push -f origin master')

print('\n Task Completed...')
