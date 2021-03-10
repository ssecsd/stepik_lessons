from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    REG_MAIL = (By.CSS_SELECTOR, '[name=registration-email]')
    REG_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password1]')
    REG_REPEAT_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password2]')
    REG_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')
    LOGIN_MAIL = (By.CSS_SELECTOR, '[name=login-username]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name=login-password]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name=login_submit]')
