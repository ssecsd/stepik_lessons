from selenium import webdriver

# Data
main_page_link = 'http://selenium1py.pythonanywhere.com/ru/'
login_page_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
profile_page_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/profile/'

alert_locator = '.alertinner'

reg_email_locator = '[name=registration-email]'
reg_password1_locator = '[name=registration-password1]'
reg_password2_locator = '[name=registration-password2]'
reg_button_locator = '[name=registration_submit]'

login_email_locator = '[name=login-username]'
login_password_locator = '[name=login-password]'
login_button_locator = '[name=login_submit]'

user_email = 'test_account_profile@example.com'
user_password = 'Pa$$w0rd!!!'
# TBD randomize email to avoid conflicts


def test_register_new_user():
    """-- Регистрация пользователя - зарегистрироваться 2.1.5"""
    # Data
    reg_success_message = 'Спасибо за регистрацию!'
    result_page_title = 'Oscar - Sandbox'

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        email = browser.find_element_by_css_selector(reg_email_locator)
        reg_password1 = browser.find_element_by_css_selector(reg_password1_locator)
        reg_password2 = browser.find_element_by_css_selector(reg_password2_locator)
        reg_button = browser.find_element_by_css_selector(reg_button_locator)

        # Act
        email.send_keys(user_email)
        reg_password1.send_keys(user_password)
        reg_password2.send_keys(user_password)
        reg_button.click()

        # Assert
        reg_success = browser.find_element_by_css_selector(alert_locator)
        assert main_page_link == browser.current_url, 'Unexpected redirect'
        assert reg_success_message == reg_success.text, 'No success message'

    finally:
        browser.quit()


def test_user_login_delete_user():
    """ -- Успешный логин 2.2.2"""
    """ -- Удаление пользователя 2.1.6"""
    # TBD Two checks in one test -> rewrite. Now it's teardown-like
    # Data
    logged_delete_user_locator = '[id=delete_profile]'
    logged_delete_password_input_locator = '[id=id_password]'
    logged_delete_confirm_locator = '.btn-danger'

    deleted_message = 'Ваш профиль удален. Спасибо, что воспользовались нашим сайтом.'

    try:
        # Login test
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_page_link)

        email = browser.find_element_by_css_selector(login_email_locator)
        password = browser.find_element_by_css_selector(login_password_locator)
        log_button = browser.find_element_by_css_selector(login_button_locator)

        # Act
        email.send_keys(user_email)
        password.send_keys(user_password)
        log_button.click()

        # Assert
        assert main_page_link == browser.current_url

        # Delete user test
        # Arrange
        browser.get(profile_page_link)
        delete_button1 = browser.find_element_by_css_selector(logged_delete_user_locator)

        # Act
        delete_button1.click()
        password_confrim = browser.find_element_by_css_selector(logged_delete_password_input_locator)
        delete_button2 = browser.find_element_by_css_selector(logged_delete_confirm_locator)
        password_confrim.send_keys(user_password)
        delete_button2.click()

        # Assert
        del_success = browser.find_element_by_css_selector(alert_locator)
        assert main_page_link == browser.current_url, 'Unexpected redirect'
        assert deleted_message in del_success.text, 'No deletion sucess message'

    finally:
        browser.quit()


if __name__ == '__main__':
    test_register_new_user()
    test_user_login_delete_user()