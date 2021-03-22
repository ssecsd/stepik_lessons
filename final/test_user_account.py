from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.locators import URLLocators
from time import sleep


class TestUserAccount:

    def test_guest_can_create_account(self, browser):
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.check_is_login_page()
        page.register_new_user()
        page.go_to_account_page()
        profile_page = AccountPage(browser, browser.current_url)
        profile_page.check_account_profile_page()

    def test_user_can_login(self, browser):
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        page.logout_user()
        page.check_is_user_logged_out()
        page.go_to_login_page()
        page.login_user()
        page.check_is_user_logged_in()

    def test_user_can_logout(self, browser):
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        page.logout_user()
        page.check_is_user_logged_out()

    def test_guest_can_delete_account(self, browser):
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        page.go_to_account_page()
        profile_page = AccountPage(browser, browser.current_url)
        profile_page.delete_user_account()
        profile_page.check_is_user_logged_out()

    def test_user_cant_register_with_weak_password(self, browser):
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user(weak_password=True)
        page.check_is_user_logged_in()
        page.check_registration_error()