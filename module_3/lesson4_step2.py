from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


link = 'http://suninjuly.github.io/selects2.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    print(num1, num2)
    answer = num1 + num2

    dropdown = Select(browser.find_element_by_tag_name('select'))
    print(dropdown)
    dropdown.select_by_value(str(answer))

    browser.find_element_by_class_name('btn-default').click()


except:
    sleep(10)
    browser.quit()
