from locators import Locator, Link
from random import randint


def get_email_password():
    user_email = f'test_email{randint(0, 99999)}@example.com'
    user_password = 'Pa$$w0rd!!!'
    return user_email, user_password


def logout(browser):

    browser.find_element(*Locator.logout_link).click()


def login_user(browser, email, password):

    browser.get(Link.login_page)
    email_field = browser.find_element(*Locator.login_email)
    password_field = browser.find_element(*Locator.login_password)
    log_button = browser.find_element(*Locator.login_button)
    email_field.send_keys(email)
    password_field.send_keys(password)
    log_button.click()


def register_new_user(browser, email, password):

    browser.get(Link.login_page)
    email_field = browser.find_element(*Locator.reg_email)
    reg_password_field = browser.find_element(*Locator.reg_password)
    reg_password_repeat_field = browser.find_element(*Locator.reg_repeat_password)
    reg_button = browser.find_element(*Locator.reg_button)

    email_field.send_keys(email)
    reg_password_field.send_keys(password)
    reg_password_repeat_field.send_keys(password)
    reg_button.click()


def test_register_new_user(browser):
    """-- Регистрация пользователя - зарегистрироваться 2.1.5"""
    # Arrange
    user_email, user_password = get_email_password()
    # Act
    register_new_user(browser, user_email, user_password)

    # Assert
    logout_icon = browser.find_element(*Locator.logout_icon)
    profile_icon = browser.find_element(*Locator.profile_icon)

    assert logout_icon and profile_icon, 'User not logged in'


def test_user_login(browser):
    """ -- Успешный логин 2.2.2"""
    # Arrange
    user_email, user_password = get_email_password()
    register_new_user(browser, user_email, user_password)
    logout(browser)

    # Act
    login_user(browser, user_email, user_password)

    # Assert
    logout_icon = browser.find_element(*Locator.logout_icon)
    profile_icon = browser.find_element(*Locator.profile_icon)
    assert logout_icon and profile_icon, 'User not logged in'


def test_delete_user(browser):
    """ -- Удаление пользователя 2.1.6"""

    # Arrange
    user_email, user_password = get_email_password()
    register_new_user(browser, user_email, user_password)
    # login_user(browser, user_email, user_password)
    # Act

    browser.get(Link.profile_page)
    delete_button = browser.find_element(*Locator.logged_delete_user)

    # Act
    delete_button.click()
    password_confirm = browser.find_element(*Locator.logged_delete_password_input)
    delete_confirm_button = browser.find_element(*Locator.logged_delete_confirm)
    password_confirm.send_keys(user_password)
    delete_confirm_button.click()
    login_user(browser, user_email, user_password)

    # Assert
    signin_icon = browser.find_element(*Locator.signin_icon)

    assert signin_icon, 'User logged in'


def test_email_validation(browser):
    # TBD Parametrize it
    # Data
    user_email, user_password = get_email_password()
    # Make password invalid
    user_password = 'test@example'

    # Act
    register_new_user(browser, user_password, user_password)

    # Assert
    signin_icon = browser.find_element(*Locator.signin_icon)
    reg_error = browser.find_element(*Locator.reg_error)

    assert signin_icon, 'Account was created with weak password'
    assert reg_error, 'No error on incorrect password'
