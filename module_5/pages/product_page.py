from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):

    def add_to_wishlist(self):
        pass

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_alert_product_name(self):
        alert_product_name = self.browser.find_element(*ProductPageLocators.BASKET_SUCCESS_ALERT)
        return alert_product_name.text

    def check_success_alert_present(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUCCESS_ALERT),\
            'No success basket alert'

    def check_product_and_alert_same(self):
        assert self.get_product_name() in self.get_alert_product_name(),\
            'Alert product not the same as page product name'

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