from selenium import webdriver
from math import log, sin
from time import sleep

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name('firstname').send_keys('First')
    browser.find_element_by_name('lastname').send_keys('Last')
    browser.find_element_by_name('email').send_keys('email@example.com')



except:
    sleep(10)
    browser.quit()
