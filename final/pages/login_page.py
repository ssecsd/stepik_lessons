from .base_page import BasePage
from .locators import LoginPageLocators
from .helpers import helper


class LoginPage(BasePage):

    def __init__(self, browser, timeout=10):
        super().__init__(browser, timeout)
        self.valid_password = helper.get_valid_password()
        self.invalid_password = helper.get_weak_password()
        self.email = helper.generate_valid_email()

    def check_is_login_page(self):
        self.check_is_login_url()
        self.check_is_login_form()
        self.check_is_register_form()

    def check_is_login_url(self):
        assert self.is_string_in_current_url('login'), \
            'No \"login\" string in url'

    def check_is_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL), \
            'No email in login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            'No password in login form'

    def check_is_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_MAIL), \
            'No email in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), \
            'No password in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_REPEAT_PASSWORD), \
            'No password confirmation in registration form'

    def check_registration_error(self):
        assert self.is_element_present(*LoginPageLocators.REG_ERROR), \
            'No error message'

    def login_user(self):
        login_email_field = self.browser.find_element(*LoginPageLocators.LOGIN_MAIL)
        login_password_field = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD)
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login_email_field.send_keys(self.email)
        login_password_field.send_keys(self.valid_password)
        login_button.click()

    def register_new_user(self, weak_password=False):
        reg_email_field = self.browser.find_element(*LoginPageLocators.REG_MAIL)
        reg_password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        reg_password_repeat_field = self.browser.find_element(*LoginPageLocators.REG_REPEAT_PASSWORD)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_email_field.send_keys(self.email)
        if not weak_password:
            reg_password_field.send_keys(self.valid_password)
            reg_password_repeat_field.send_keys(self.valid_password)
        else:
            reg_password_field.send_keys(self.invalid_password)
            reg_password_repeat_field.send_keys(self.invalid_password)
        reg_button.click()
