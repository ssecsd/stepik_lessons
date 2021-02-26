import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

param = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

def calc():
    answer = math.log(int(time.time()))
    return answer

def setup_module():
    print('start browser')
    global browser
    browser = webdriver.Chrome()

def teardown_module():
    print('quit')

@pytest.mark.parametrize('link', param)
def test_page(link):
    browser.get(link)
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea'))
    )
    browser.find_element_by_css_selector('textarea').send_keys(str(calc()))
    browser.find_element_by_css_selector('.submit-submission').click()
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
    )
    response = browser.find_element_by_css_selector('.smart-hints__hint')
    assert response.text == 'Correct!', f'Text is {response.text} not "Correct!"'