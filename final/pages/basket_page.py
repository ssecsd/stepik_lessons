from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE),\
            'Basket not empty'

    def check_basket_not_have_checkout(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CHECKOUT_BUTTON), \
            'Basket can be checked out'
