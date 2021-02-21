import math
from time import sleep

from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    x = browser.find_element_by_id("input_value").text
    print(x)
    answer = math.log(abs(12 * math.sin(int(x))))
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
