from selenium.webdriver.common.by import By


class Locator:
    # Nav-bar icons
    logout_icon = (By.CSS_SELECTOR, '.icon-signout')
    profile_icon = (By.CSS_SELECTOR, '.icon-user')
    signin_icon = (By.CSS_SELECTOR, '.icon-signin')

    logout_link = (By.CSS_SELECTOR, '#logout_link')

    # Login/register page fields
    reg_email = (By.CSS_SELECTOR, '[name=registration-email]')
    reg_password = (By.CSS_SELECTOR, '[name=registration-password1]')
    reg_repeat_password = (By.CSS_SELECTOR, '[name=registration-password2]')
    reg_button = (By.CSS_SELECTOR, '[name=registration_submit]')
    login_email = (By.CSS_SELECTOR, '[name=login-username]')
    login_password = (By.CSS_SELECTOR, '[name=login-password]')
    login_button = (By.CSS_SELECTOR, '[name=login_submit]')

    # Login/register page alerts
    reg_alert = (By.CSS_SELECTOR, '#register_form>.alert-danger')
    reg_error = (By.CSS_SELECTOR, '#register_form>.has-error .error-block')

    # Account page
    logged_delete_user = (By.CSS_SELECTOR, '#delete_profile')
    logged_delete_password_input = (By.CSS_SELECTOR, '#id_password')
    logged_delete_confirm = (By.CSS_SELECTOR, '.btn-danger')


class Link:
    main_page = f'http://selenium1py.pythonanywhere.com/'
    login_page = main_page + f'/accounts/login/'
    profile_page = main_page + f'accounts/profile/'
