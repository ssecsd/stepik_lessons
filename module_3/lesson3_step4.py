from selenium import webdriver
import math
from time import sleep

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    print(x)
    answer = math.log(abs(12*math.sin(int(x))))
    print(answer)
    captcha = browser.find_element_by_id('answer')
    captcha.send_keys(str(answer))
    robotCheckbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    robotCheckbox.click()
    robotsRule = browser.find_element_by_css_selector('[for="robotsRule"]')
    robotsRule.click()
    button = browser.find_element_by_class_name('btn-default')
    button.click()

except:
    sleep(30)
    browser.quit()
