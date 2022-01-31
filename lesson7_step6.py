from selenium import webdriver
import time
import math

# В процессе

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_css_selector("valuex")
    x = x_element.text
    y = calc(x)

    result = browser.find_element_by_class_name("form-control")
    result.send_keys(y)

finally:
    time.sleep(10)
    browser.quit()
