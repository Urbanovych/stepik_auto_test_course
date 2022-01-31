from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Работает 31.01.2022

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(12)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    #тема урока
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element_by_id("book")
    button.click()

    number = browser.find_element_by_id("input_value")
    x = calc(number.text)
    inputnum = browser.find_element_by_class_name("form-control")
    inputnum.send_keys(x)
    submit = browser.find_element_by_id("solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
