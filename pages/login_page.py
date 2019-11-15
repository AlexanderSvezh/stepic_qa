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

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.USER_ICON), "User icon is not presented"

    def register_new_user(self, login, password):
        mail = self.browser.find_element(*LoginPageLocators.REG_MAIL)
        mail.send_keys("{}{}@fakemail.ru".format(login, time.time()))
        pwd = self.browser.find_element(*LoginPageLocators.REG_PASS)
        pwd.send_keys(password)
        confirm_pwd = self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM)
        confirm_pwd.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_SUBMIT).click()
        self.should_be_authorized_user()
