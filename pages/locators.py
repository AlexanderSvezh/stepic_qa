from selenium.webdriver.common.by import By


class MainPageLocators:
    LOG_LINK = (By.CSS_SELECTOR, "#login_link")
    REG_LINK = (By.CSS_SELECTOR, "#registration_link")
    MAIN_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    MAIN_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class LoginPageLocators:
    LOG_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')
    REG_MAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REG_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REG_PASS_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_SUBMIT = (By.NAME, 'registration_submit')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')


class BasketPageLocators:
    BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_NAME = (By.CSS_SELECTOR, '.basket-items h3 a')
    BASKET_PRICE = (By.CSS_SELECTOR, '.basket-items .price_color')
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MINI = (By.CSS_SELECTOR, ".basket-mini")