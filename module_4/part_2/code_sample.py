import pytest
from selenium import webdriver
from random import randint
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def get_email_password():
    user_email = f'test_email{randint(0, 99999)}@example.com'
    user_password = 'Pa$$w0rd!!!'
    return user_email, user_password

def test_register_new_user(browser):
    """-- Регистрация пользователя - зарегистрироваться 2.1.5"""
    # Data
    logout_icon_locator = (By.CSS_SELECTOR, '.icon-signout')
    logout_link_locator = (By.CSS_SELECTOR, '#logout_link')

    reg_email = (By.CSS_SELECTOR, '[name=registration-email]')
    reg_password = (By.CSS_SELECTOR, '[name=registration-password1]')
    reg_repeat_password = (By.CSS_SELECTOR, '[name=registration-password2]')
    reg_button = (By.CSS_SELECTOR, '[name=registration_submit]')

    login_page = f'http://selenium1py.pythonanywhere.com/accounts/login/'
    user_email, user_password = get_email_password()

    # Arrange
    browser.get(login_page)
    email_field = browser.find_element(*reg_email)
    reg_password = browser.find_element(*reg_password)
    reg_password_repeat = browser.find_element(*reg_repeat_password)
    reg_button = browser.find_element(*reg_button)

    # Act
    email_field.send_keys(user_email)
    reg_password.send_keys(user_password)
    reg_password_repeat.send_keys(user_password)
    reg_button.click()

    # Assert
    logout_icon = browser.find_element(*logout_icon_locator)
    logout_link = browser.find_element(*logout_link_locator)

    assert logout_icon and logout_link, 'User not logged in'