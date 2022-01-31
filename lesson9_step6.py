from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    time.sleep(1)
    btn1 = browser.find_element_by_class_name("trollface")
    btn1.click()

    # Переход к новому окну
    new_window = browser.window_handles[1]
    # Переключение Селениума на новое окно (пока это не сделать - все операции после переключения будут работать в старой вкладке)
    browser.switch_to.window(new_window)

    time.sleep(1)
    number = browser.find_element_by_id("input_value")
    x = calc(number.text)

    inputnum = browser.find_element_by_class_name("form-control")
    inputnum.send_keys(x)

    submit = browser.find_element_by_class_name("btn-primary")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
