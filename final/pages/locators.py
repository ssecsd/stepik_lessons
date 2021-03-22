from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGOUT_LINK = (By.CSS_SELECTOR, '#logout_link')
    ACCOUNT_LINK = (By.CSS_SELECTOR, '.navbar-right li:nth-child(1) a')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, '.basket-mini a:nth-child(1)')


class URLLocators:
    MAIN_URL = 'http://selenium1py.pythonanywhere.com'
    LOGIN_PATH = '/accounts/login/'
    ACCOUNT_PATH = '/accounts/profile/'
    BASKET_PATH = '/basket/'
    LOGIN_URL = MAIN_URL + LOGIN_PATH
    ACCOUNT_URL = MAIN_URL + ACCOUNT_PATH
    BASKET_URL = MAIN_URL + BASKET_PATH


class MainPageLocators(BasePageLocators):
    def __init__(self, *args, **kwargs):
        super(BasePageLocators, self).__init__(*args, **kwargs)


class LoginPageLocators(BasePageLocators):
    REG_MAIL = (By.CSS_SELECTOR, '[name=registration-email]')
    REG_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password1]')
    REG_REPEAT_PASSWORD = (By.CSS_SELECTOR, '[name=registration-password2]')
    REG_BUTTON = (By.CSS_SELECTOR, '[name=registration_submit]')
    LOGIN_MAIL = (By.CSS_SELECTOR, '[name=login-username]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name=login-password]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name=login_submit]')
    REG_ALERT = (By.CSS_SELECTOR, '#register_form>.alert-danger')
    REG_ERROR = (By.CSS_SELECTOR, '#register_form>.has-error .error-block')


class ProductPageLocators(BasePageLocators):
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form > button')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_SUCCESS_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(1)')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert:nth-child(1) strong')
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, '#messages .alert:nth-child(3)')
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, '#messages .alert:nth-child(3) strong')
    VIEW_BASKET_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(1)')
    CHECKOUT_NOW_FROM_ALERT = (By.CSS_SELECTOR, '.alertinner p a:nth-child(2)')


class BasketPageLocators(BasePageLocators):
    BASKET_ALERT = (By.CSS_SELECTOR, '.alertinner')
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content > #content_inner')
    BASKET_VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(1)')
    BASKET_CHECKOUT_BUTTON = (By.CSS_SELECTOR, 'p:nth-child(2) >a:nth-child(2)')
    BASKET_ORDER_TOTAL = (By.CSS_SELECTOR, '.total > .price_color')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p:nth-child(1)')


class AccountPageLocators(BasePageLocators):
    DELETE_PROFILE_BUTTON = (By.CSS_SELECTOR, '#delete_profile')
    DELETE_PASSWORD = (By.CSS_SELECTOR, '#id_password')
    DELETE_CONFIRM = (By.CSS_SELECTOR, '.btn-danger')
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, '')