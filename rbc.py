import os, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ["PATH"] += ":"+os.path.abspath(os.path.join(os.getcwd(), os.pardir))


driver = webdriver.Firefox()
driver.get("http://www.rbcbank.com/index.page")
print driver.current_url
driver.find_element_by_link_text("Sign In").click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "K1"))
    )
    print driver.current_url
    username = driver.find_element_by_xpath('//*[@id="K1"]')
    password = driver.find_element_by_xpath('//*[@id="Q1"]')

    username.send_keys("YourUsername")
    password.send_keys("Pa55worD")

    driver.find_element_by_name("Sign In").click()

finally:
    driver.close()
