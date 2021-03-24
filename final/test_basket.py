from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import URLLocators
import pytest


class TestBasket:

    def test_change_item_quantity_in_basket(self, browser):
        # Arrange
        page = ProductPage(browser, URLLocators.PRODUCT_URL)
        page.open()
        page.add_to_basket()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        # Act
        item_quantity = 3
        basket_page.change_quantity_to(item_quantity)
        # Assert
        basket_page.check_total_items_price_is_correct(item_quantity)

    @pytest.mark.xfail
    def test_item_can_be_deleted_from_basket(self, browser):
        # Arrange
        page = ProductPage(browser, URLLocators.PRODUCT_URL)
        page.open()
        page.add_to_basket()
        page.go_to_basket()
        # Act
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.delete_item_from_basket()
        # Assert
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()
