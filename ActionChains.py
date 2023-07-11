import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://seleniumbase.io/demo_page")

hoverDrop = driver.find_element(By.ID, 'myDropdown')
# hoverDrop.click()
drop3 = driver.find_element(By.ID, 'dropOption3')
# drop3.click()

actionObj = ActionChains(driver)
actionObj.move_to_element(hoverDrop).move_to_element(drop3).click().perform()
