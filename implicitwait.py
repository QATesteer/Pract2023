import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)


driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.implicitly_wait(10)

btnElement = driver.find_element(By.XPATH, '//*[@id="start"]/button')
btnElement.click()

load = driver.find_element(By.XPATH,'//*[@id="loading"]')
print(load.get_attribute("innerHTML"))
# time.sleep(5)

element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(element.get_attribute("innerHTML"))


# ele = WebDriverWait(driver,10).until.(EC.presence_of_element_located(By.XPATH,''))