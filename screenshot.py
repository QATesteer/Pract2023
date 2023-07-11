from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.facebook.com")
# option1

driver.save_screenshot("fb.png")

# option2

driver.get_screenshot_as_file("D:\pic\fb.png")
## option3
# driver.get_screenshot_as_png("fb.png")
# driver.get_screenshot_as_base64("fb.png")
