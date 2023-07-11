from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/windows")

first_Page = driver.find_element(By.LINK_TEXT, 'Click Here')
first_Page.click()

all_handles = driver.window_handles

print("all window handle: ", all_handles)

print("current window handle: ", driver.current_window_handle)

driver.switch_to.window(all_handles[-1])
sec_page = driver.find_element(By.XPATH, '/html/body/div/h3')
print(sec_page.text)
print(sec_page.get_attribute('innerHTML'))
