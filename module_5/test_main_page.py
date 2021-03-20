from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_check_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.check_login_link()


class TestBasketFromMainPage:

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_basket_empty_message()
        basket_page.check_basket_not_have_checkout()
