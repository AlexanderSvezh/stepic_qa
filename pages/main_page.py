from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOG_LINK)
        login_link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.REG_LINK), "Login link is not presented"

    def get_main_name(self):
        return self.browser.find_element(*MainPageLocators.MAIN_NAME).text

    def get_main_price(self):
        return self.browser.find_element(*MainPageLocators.MAIN_PRICE).text

    def click_add_product_to_basket(self):
        self.browser.find_element(*BasketPageLocators.BASKET).click()
