import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
driver.maximize_window()
frame2 = driver.find_element(By.ID,"iframeResult")
driver.switch_to.frame(frame2)
btnElement = driver.find_element(By.XPATH,"/html/body/button")
btnElement.click()


