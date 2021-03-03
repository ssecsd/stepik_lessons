from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_add_to_basket_localization(browser):
    # Data
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    add_to_basket_loc = {'ru': 'Добавить в корзину', 'en-gb': 'Add to basket',
                         'es': 'Añadir al carrito', 'fr': 'Ajouter au panier'}
    # Arrange
    browser.get(link)

    # Act
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket')))

    add_to_basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
    # Assert
    url_splitted = browser.current_url.split('/')
    current_locale = url_splitted[3]

    assert current_locale in add_to_basket_loc, f'{current_locale} not supported in this case'
    assert add_to_basket_button.text == add_to_basket_loc[
        current_locale], f'{add_to_basket_loc[current_locale]} not equal {add_to_basket_button.text}'
