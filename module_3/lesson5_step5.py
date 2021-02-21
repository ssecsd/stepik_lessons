from math import log, sin
from time import sleep

from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_class_name('trollface').click()
    browser.switch_to.window(browser.window_handles[1])

    x = browser.find_element_by_id("input_value").text
    answer = log(abs(12 * sin(int(x))))
    captcha = browser.find_element_by_id('answer')
    captcha.send_keys(str(answer))
    button = browser.find_element_by_tag_name('button')
    button.click()

except:
    sleep(30)
    browser.quit()
