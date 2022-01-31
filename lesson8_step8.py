from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Yaroslav")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Urbanovych")
    email = browser.find_element_by_name("email")
    email.send_keys("urbanovych.qa@gmail.com")

    file = browser.find_element_by_name("file")
    # Назначение пути файла в переменную через os
    filetxt = os.path.abspath('file.txt')
    file.send_keys(filetxt)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
