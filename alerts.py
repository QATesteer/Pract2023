
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

elementbtn = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/ul/li[1]/button")   ##/*[@id="content"]/div/ul/li[1]/button
elementbtn.click()

#driver.switch_to.alert.accept()  ## click on accept = OK
driver.switch_to.alert.dismiss()  ## click on cancel

