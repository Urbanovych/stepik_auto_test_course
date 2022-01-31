from selenium import webdriver
import time
import math

# Не находит число в сундуке

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    number = browser.find_element_by_id("treasure")
    number.get_attribute('valuex')
    x = calc(number.text)

    result = browser.find_element_by_id("answer")
    result.send_keys(str(x))

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
