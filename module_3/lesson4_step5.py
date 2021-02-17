from selenium import webdriver
from math import log, sin
from time import sleep

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    print(x)
    answer = log(abs(12*sin(int(x))))
    browser.find_element_by_id('answer').send_keys(str(answer))
    browser.execute_script("window.scrollBy(0, 150);")
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()



    browser.find_element_by_class_name('btn-primary').click()


except:
    sleep(10)
    browser.quit()
