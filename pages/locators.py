from selenium.webdriver.common.by import By


class MainPageLocators:
    LOG_LINK = (By.CSS_SELECTOR, "#login_link")
    REG_LINK = (By.CSS_SELECTOR, "#registration_link")
    MAIN_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    MAIN_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alertinner')


class LoginPageLocators:
    LOG_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')


class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_NAME = (By.CSS_SELECTOR, '.basket-items h3 a')
    BASKET_PRICE = (By.CSS_SELECTOR, '.basket-items .price_color')