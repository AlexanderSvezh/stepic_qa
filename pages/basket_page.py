from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def get_basket_name(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_NAME).text

    def get_basket_price(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_PRICE).text

    def is_empty_basket(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text

