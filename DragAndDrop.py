from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

actOb = ActionChains(driver)

dropbox5 = driver.find_element(By.ID, "box5")

dropbox6 = driver.find_element(By.ID, "box102")

actOb.drag_and_drop(dropbox5,dropbox6).perform()
