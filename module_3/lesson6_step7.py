from math import log, sin
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
try:

    browser.get(link)
    price = browser.find_element_by_id('price')

    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_id('book').click()

    x = browser.find_element_by_id("input_value").text
    answer = log(abs(12 * sin(int(x))))
    captcha = browser.find_element_by_id('answer')
    captcha.send_keys(str(answer))
    button = browser.find_element_by_id('solve')
    button.click()


except:
    sleep(30)
    browser.quit()
