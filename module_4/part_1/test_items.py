from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import warnings


def test_add_to_basket_localization(browser, user_language):
    # Data
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    add_to_basket_loc = {'ru': 'Добавить в корзину', 'en-gb': 'Add to basket',
                         'es': 'Añadir al carrito', 'fr': 'Ajouter au panier'}
    add_to_basket_button_locator = (By.CSS_SELECTOR, '.btn-add-to-basket')

    # Arrange
    browser.get(link)
    print(user_language)

    # Act
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(add_to_basket_button_locator))

    add_to_basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')

    # Assert
    assert user_language in add_to_basket_loc, f'{user_language} not supported in this case'
    assert add_to_basket_button.text == add_to_basket_loc[
        user_language], f'{add_to_basket_loc[user_language]} not equal {add_to_basket_button.text}'
