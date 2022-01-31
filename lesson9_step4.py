from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    btn1 = browser.find_element_by_class_name("btn-primary")
    btn1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    number = browser.find_element_by_id("input_value")
    x = calc(number.text)

    inputnum = browser.find_element_by_class_name("form-control")
    inputnum.send_keys(x)

    submit = browser.find_element_by_class_name("btn-primary")
    submit.click()

finally:
    time.sleep(7)
    browser.quit()
