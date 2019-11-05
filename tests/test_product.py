import pytest
from pages import MainPage
from pages import BasketPage


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.need_review
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


def test_user_can_add_product_to_basket():
    pass


def test_guest_can_add_product_to_basket():
    pass


def test_guest_cant_see_product_in_basket_opened_from_product_page():
    pass


def test_guest_can_go_to_login_page_from_product_page():
    pass