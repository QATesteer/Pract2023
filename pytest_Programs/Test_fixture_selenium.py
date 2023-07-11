import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


@pytest.fixture()
def setup():
    global driver
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    print("get driver")
    print("maximize window")
    yield  # divide before and after activity
    print(driver.title)
    # driver.close()


def test_1(setup):
    driver.get("https://www.facebook.com")


def test_2(setup):
    driver.get("https://www.amazon.com")


def test_3(setup):
    driver.get("https://www.gmail.com")
