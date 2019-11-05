from pages import MainPage
from pages import LoginPage
from pages.locators import MainPageLocators
import pytest


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    login_page.should_be_login_url()
    login_page.should_be_register_form()
    login_page.should_be_login_form()


def test_guest_should_see_login_link(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = MainPage(browser, link)
    page.open()
    page.click_add_product_to_basket()
    page.solve_quiz_and_get_code()


url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


def test_guest_can_add_product_to_basket_207(browser):
    link = '{}/?promo=newYear2019'.format(url)
    page = MainPage(browser, link)
    page.open()
    page.click_add_product_to_basket()
    page.solve_quiz_and_get_code()


# ToDo : create reason to xfail tests
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, url)
    page.open()
    page.click_add_product_to_basket()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, url)
    page.open()
    assert page.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, url)
    page.open()
    page.click_add_product_to_basket()
    assert page.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE)
