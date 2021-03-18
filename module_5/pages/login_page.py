from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_string_in_current_url('login'),\
            'No \"login\" string in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL),\
            'No email in login form'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD),\
            'No password in login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_MAIL),\
            'No email in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD),\
            'No password in registration form'
        assert self.is_element_present(*LoginPageLocators.REG_REPEAT_PASSWORD),\
            'No password confirmation in registration form'
