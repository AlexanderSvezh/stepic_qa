from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.LOG_FORM)

    def should_be_register_form(self):
        self.should_be_login_url()
        assert self.is_element_present(*LoginPageLocators.REG_FORM)
