from .pages.product_page import ProductPage
import pytest
from time import sleep




class TestProductPage:

    @pytest.mark.parametrize('promo_offer',
                             ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail),
                              "offer8", "offer9"])
    def test_guest_can_add_product_to_basket(self, browser, promo_offer):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        promo_link = '?promo='

        page = ProductPage(browser, link + promo_link + promo_offer)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_success_alert_present()
        page.check_product_and_alert_same()
        page.check_product_and_basket_price_same()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.check_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.check_login_link()
        page.go_to_login_page()
        assert page.is_string_in_current_url('login'), 'Not login page'
