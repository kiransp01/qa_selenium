import time
from re import search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver_path = r'C:\Drivers\chromedriver-win32\chromedriver.exe'
ser_obj = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=ser_obj)

driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@type='search']").click()

new_yk =driver.find_element(By.XPATH,"//input[@type='search']")
new_yk.send_keys("New York")
rows =len(driver.find_elements(By.XPATH,"//table[@id ='example']/tbody/tr"))
table = driver.find_element(By.XPATH,"//table[@id ='example']/tbody/tr/td").text
for r in range(1,1+rows):
    office =driver.find_element(By.XPATH,"//table[@id ='example']/tbody/tr["+str(r)+"]/td[3]").text
    if office=="New York":
        search_result = len(driver.find_elements(By.XPATH, "//table[@id ='example']/tbody/tr"))
print(search_result)


driver.close()