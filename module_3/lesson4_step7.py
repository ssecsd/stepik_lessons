from selenium import webdriver
from os import path
from time import sleep

current_dir = path.abspath(path.dirname(__file__))
file_path = path.join(current_dir, 'test.txt')

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)

try:
    browser.find_element_by_name('firstname').send_keys('First')
    browser.find_element_by_name('lastname').send_keys('Last')
    browser.find_element_by_name('email').send_keys('email@example.com')

    browser.find_element_by_name('file').send_keys(file_path)
    browser.find_element_by_tag_name('button').click()

except:
    sleep(10)
    browser.quit()
