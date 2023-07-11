import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains

options = webdriver.ChromeOptions()

options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)

driver.get("https://seleniumbase.io/demo_page")
driver.maximize_window()

driver.maximize_window()

element = driver.find_element(By.ID,"mySelect")
dropdown = Select(element)
dropdown.select_by_value('75%')

time.sleep(3)

dropdown = Select(element)
dropdown.select_by_value('50%')

time.sleep(2)

all_otions = dropdown.options

print("Number of Options: ",len(all_otions))

rdButton = driver.find_element(By.ID,'radioButton1')
print(rdButton.is_selected())

actobj = ActionChains(driver)

drpd = driver.find_element(By.ID,'myDropdown')
drpd3 = driver.find_element(By.ID,'dropOption3')
actobj.move_to_element(drpd).move_to_element(drpd3).click().perform()
link = driver.find_element(By.XPATH,'//*[@id="tbodyId"]/tr[1]/td[4]/h3')
print(link.is_displayed())

# links = driver.find_element(By.TAG_NAME,"a")
# print("Number of Links is : ",len(links))

# for item in all_otions:
#     print(item.get_attribute('innerHTML'))
#     print(item.text)
#
# links = driver.find_elements(By.TAG_NAME,"a")
# print("Number of links : ",len(links))

# driver.find_elements(By.PARTIAL_LINK_TEXT,"REG").click()