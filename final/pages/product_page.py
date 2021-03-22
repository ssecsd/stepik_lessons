import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_wishlist(self):
        pass

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def check_success_alert_present(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUCCESS_ALERT), \
            f'No success basket alert \n \n {self.browser.current_url}'

    def check_product_and_alert_same(self):
        assert self.get_product_name() == self.get_basket_product_name(), \
            f'Alert product name not the same as page product name \n {self.browser.current_url}'

    def check_product_and_basket_price_same(self):
        assert self.get_basket_price() == self.get_product_price(), f'Basket price and product price are not the same' \
                                                                    f'\n {self.browser.current_url}'

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_basket_product_name(self):
        alert_product_name = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME)
        return alert_product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE).text
        return product_price

    def get_basket_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        return basket_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_SUCCESS_ALERT), \
            'Success message is presented, but should not be'

    def should_dissapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_SUCCESS_ALERT), \
            'Success message was presented, but dissapeared'

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
