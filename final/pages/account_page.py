from .locators import AccountPageLocators, URLLocators
from .helpers import credhelper
from .base_page import BasePage


class AccountPage(BasePage):

    def delete_user_account(self):
        delete_button = self.browser.find_element(*AccountPageLocators.DELETE_PROFILE_BUTTON)
        delete_button.click()
        delete_password = self.browser.find_element(*AccountPageLocators.DELETE_PASSWORD)
        delete_confirm_button = self.browser.find_element(*AccountPageLocators.DELETE_CONFIRM)
        delete_password.send_keys(credhelper.get_valid_password())
        delete_confirm_button.click()

    def check_account_url(self):
        assert self.is_string_in_current_url(URLLocators.ACCOUNT_PATH), \
            f'No {URLLocators.ACCOUNT_PATH} string in url'

    def check_delete_profile_button(self):
        assert self.is_element_present(*AccountPageLocators.DELETE_PROFILE_BUTTON), \
            'No delete profile button'

    def check_account_profile_page(self):
        self.check_account_url()
        self.check_delete_profile_button()