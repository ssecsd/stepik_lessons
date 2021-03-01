from random import randint
from conftest import user_email, user_password
from locators import Locator, Link


def login(browser, email, password):

    browser.get(Link.login_page)
    email_field = browser.find_element(*Locator.login_email)
    password_field = browser.find_element(*Locator.login_password)
    log_button = browser.find_element(*Locator.login_button)
    email_field.send_keys(email)
    password_field.send_keys(password)
    log_button.click()


def test_register_new_user(browser):
    """-- Регистрация пользователя - зарегистрироваться 2.1.5"""
    # Arrange
    browser.get(Link.login_page)
    email_field = browser.find_element(*Locator.reg_email)
    reg_password = browser.find_element(*Locator.reg_password)
    reg_password_repeat = browser.find_element(*Locator.reg_repeat_password)
    reg_button = browser.find_element(*Locator.reg_button)

    # Act
    email_field.send_keys(user_email)
    reg_password.send_keys(user_password)
    reg_password_repeat.send_keys(user_password)
    reg_button.click()

    # Assert
    logout_icon = browser.find_element(*Locator.logout_icon)
    profile_icon = browser.find_element(*Locator.profile_icon)

    assert logout_icon and profile_icon, 'User not logged in'


def test_user_login(browser):
    """ -- Успешный логин 2.2.2"""
    # Arrange
    browser.get(Link.login_page)
    email_field = browser.find_element(*Locator.login_email)
    password_field = browser.find_element(*Locator.login_password)
    log_button = browser.find_element(*Locator.login_button)

    # Act
    email_field.send_keys(user_email)
    password_field.send_keys(user_password)
    log_button.click()

    # Assert
    logout_icon = browser.find_element(*Locator.logout_icon)
    profile_icon = browser.find_element(*Locator.profile_icon)
    assert logout_icon and profile_icon, 'User not logged in'


def test_delete_user(browser):
    """ -- Удаление пользователя 2.1.6"""

    # Arrange
    login(browser, user_email, user_password)
    # Act

    browser.get(Link.profile_page)
    delete_button = browser.find_element(*Locator.logged_delete_user)

    # Act
    delete_button.click()
    password_confirm = browser.find_element(*Locator.logged_delete_password_input)
    delete_confirm_button = browser.find_element(*Locator.logged_delete_confirm)
    password_confirm.send_keys(user_password)
    delete_confirm_button.click()
    login(browser, user_email, user_password)

    # Assert
    signin_icon = browser.find_element(*Locator.signin_icon)

    assert signin_icon, 'User logged in'

def test_email_validation(browser):
    # TBD Parametrize it
    # Data
    user_wrong_email = 'test@example'
    wrong_email_alert_locator = '#register_form .error-block'

    browser.get(Link.login_page)

    # Arrange
    email = browser.find_element(*Locator.reg_email)
    reg_password = browser.find_element(*Locator.reg_password)
    reg_password_repeat = browser.find_element(*Locator.reg_repeat_password)
    reg_button = browser.find_element(*Locator.reg_button)

    # Act
    email.send_keys(user_wrong_email)
    reg_password.send_keys(user_password)
    reg_password_repeat.send_keys(user_password)
    reg_button.click()

    # Assert
    signin_icon = browser.find_element(*Locator.signin_icon)
    reg_error = browser.find_element(*Locator.reg_error)

    assert signin_icon, 'Account be created with weak password'
    assert reg_error, 'No error on incorrect password'
