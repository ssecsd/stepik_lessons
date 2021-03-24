from .base_page import BasePage
from .locators import BasketPageLocators
from .helpers import helper


class BasketPage(BasePage):

    def change_quantity_to(self, quantity: int):
        item_quantity = self.browser.find_element(*BasketPageLocators.BASKET_ITEM_QUANTITY)
        update_quantity = self.browser.find_element(*BasketPageLocators.BASKET_QUANTITY_UPDATE)
        item_quantity.click()
        item_quantity.clear()
        item_quantity.send_keys(str(quantity))
        update_quantity.click()

    def check_total_items_price_is_correct(self, quantity: int):
        item_price = self.browser.find_element(*BasketPageLocators.BASKET_ITEM_PRICE)
        total_items_price = self.browser.find_element(*BasketPageLocators.BASKET_ITEM_TOTAL_PRICE)
        item_price = helper.strip_price_to_float(item_price.text)
        total_items_price = helper.strip_price_to_float(total_items_price.text)
        assert float(total_items_price) == float(item_price) * quantity, \
            'Total price not correct'

    def delete_item_from_basket(self):
        delete_button = self.browser.find_element(*BasketPageLocators.BASKET_ITEM_DELETE)
        delete_button.click()

    def check_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), \
            'Basket not empty'

    def check_basket_not_have_checkout(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CHECKOUT_BUTTON), \
            'Basket can be checked out'
