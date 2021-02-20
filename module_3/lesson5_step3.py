from selenium import webdriver
from time import sleep
from math import log, sin

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_class_name('btn-primary').click()
    browser.switch_to.alert.accept()

    x = browser.find_element_by_id("input_value").text
    print(x)
    answer = log(abs(12*sin(int(x))))
    print(answer)
    captcha = browser.find_element_by_id('answer')
    captcha.send_keys(str(answer))
    button = browser.find_element_by_tag_name('button')
    button.click()

except:
    sleep(30)
    browser.quit()


