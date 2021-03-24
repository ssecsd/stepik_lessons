from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.locators import URLLocators
import pytest


class TestUserAccount:

    def test_guest_can_create_account(self, browser):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.check_is_login_page()
        # Act
        page.register_new_user()
        page.go_to_account_page()
        # Assert
        profile_page = AccountPage(browser, browser.current_url)
        profile_page.check_account_profile_page()

    def test_user_can_login(self, browser):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        page.logout_user()
        page.check_is_user_logged_out()
        # Act
        page.go_to_login_page()
        page.login_user()
        # Assert
        page.check_is_user_logged_in()

    def test_user_can_logout(self, browser):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        # Act
        page.logout_user()
        # Assert
        page.check_is_user_logged_out()

    def test_guest_can_delete_account(self, browser):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        page.register_new_user()
        page.go_to_account_page()
        # Act
        profile_page = AccountPage(browser, browser.current_url)
        profile_page.delete_user_account()
        # Assert
        profile_page.check_is_user_logged_out()

    def test_user_cant_register_with_weak_password(self, browser):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        # Act
        page.register_new_user(weak_password=True)
        # Assert
        page.check_is_user_logged_in()
        page.check_registration_error()

    @pytest.mark.parametrize('email_param',
        ['email@test', '@test.com', 'example',
         'email.@test.', 'email.x@test'])
    def test_email_validation(self, browser, email_param):
        # Arrange
        page = LoginPage(browser, URLLocators.LOGIN_URL)
        page.open()
        # Act
        page.email = email_param
        page.register_new_user()
        # Assert
        page.check_is_user_logged_out()
