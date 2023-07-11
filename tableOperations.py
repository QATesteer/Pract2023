from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/html/html_tables.asp")
# driver.maximize_window()

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').text)
print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[2]').get_attribute("innerHTML"))

eleList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')

print("Number of rows len: ", len(eleList))
print("Number of rows elements : ", eleList.__len__())

eleList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th')

print("Number of columns len: ", len(eleList))
print("Number of columns elements: ", eleList.__len__())

eleList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td')

print("Number of rows len: ", len(eleList))
print("Number of rows element: ", eleList.__len__())
