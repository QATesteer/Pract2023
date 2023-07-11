import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

btnElement = driver.find_element(By.XPATH, '//*[@id="start"]/button')
btnElement.click()

load = By.XPATH, '//*[@id="loading"]'
element = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(load))
#.until(expected_conditions.visibility_of_element_located(load))
print(element.get_attribute("innerHTML"))


load2 = By.XPATH, '//*[@id="finish"]/h4'
element2 = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(load2))
print(element.get_attribute("innerHTML"))

