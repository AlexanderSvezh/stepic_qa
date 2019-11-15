import pytest
from pages import MainPage
from pages import BasketPage
from pages import LoginPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.parametrize('link', ["{}/?promo=offer0".format(url),
                                  "{}/?promo=offer1".format(url),
                                  "{}/?promo=offer2".format(url),
                                  "{}/?promo=offer3".format(url),
                                  "{}/?promo=offer4".format(url),
                                  "{}/?promo=offer5".format(url),
                                  "{}/?promo=offer6".format(url),
                                  "{}/?promo=offer8".format(url),
                                  "{}/?promo=offer9".format(url),
                                  pytest.param("{}/?promo=offer7".format(url), marks=pytest.mark.xfail)
                                  ])
def test_guest_can_add_product_to_basket_parametrize(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_add_product_to_basket()
    page.solve_quiz_and_get_code()
    product_main_name = page.get_main_name()
    basket_link = 'http://selenium1py.pythonanywhere.com/ru/basket/'
    basket_page = BasketPage(browser, basket_link)
    basket_page.open()
    basket_product_name = basket_page.get_basket_name()
    assert basket_product_name == product_main_name


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    page.click_add_product_to_basket()
    page.solve_quiz_and_get_code()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = MainPage(browser, url)
    page.open()
    empty_basket = 'Basket total: £0.00\nView basket'
    assert empty_basket in page.check_empty_basket(), 'guest can see product in basket'


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user('Alex', 'A1q345sdfvw')
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, url)
        page.open()
        page.click_add_product_to_basket()
        empty_basket = 'Basket total: £0.00\nView basket'
        assert empty_basket not in page.check_empty_basket(), 'product is not added'

    def test_user_cant_see_success_message(self, browser):
        page = MainPage(browser, url)
        page.open()
        assert page.is_success_message()
