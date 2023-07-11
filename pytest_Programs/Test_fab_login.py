from selenium import webdriver
from selenium.webdriver.common.by import By


def test_Login():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get('https://www.facebook.com')
    inputEmail = driver.find_element(By.ID, "email")
    inputEmail.send_keys("asfd@gmail.com")

    inputPass = driver.find_element(By.ID, "pass")
    inputPass.send_keys("Passward@123")

    login = driver.find_element(By.NAME, "login").click()

