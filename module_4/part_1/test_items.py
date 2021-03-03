from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_item_has_addtobasket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))
    url_splitted = browser.current_url.split('/')

    add_to_basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    if 'ru' in url_splitted:
        assert add_to_basket_button.text == 'Добавить в корзину', "Wrong 'Add to basket' naming"
    elif 'en-gb' in url_splitted:
        assert add_to_basket_button.text == 'Add to basket', "Wrong 'Add to basket' naming"
    else:
        assert True, 'Incorrect url or language test not implemented'

