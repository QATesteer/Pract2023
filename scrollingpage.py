import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

time.sleep(3)
driver.execute_script('window.scrollBy(0,3000)', " ")

time.sleep(2)

ele = driver.find_element(By.ID, "Syntax_and_semantics")
driver.execute_script("arguments[0].scrollIntoView()", ele)

# driver.execute_script('window.scrollBy(0,1500)'," ")

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
