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


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    # TODO: Rework. It's based on alerts order that may change
    BASKET_SUCCESS_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3)')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')
    VIEW_BASKET_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(1)')
    CHECKOUT_NOW_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(2)')
