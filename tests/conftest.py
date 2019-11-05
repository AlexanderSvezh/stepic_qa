import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='es',
                     help="Choose lang")


@pytest.fixture(scope='function')
def browser():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(executable_path='./chromedriver', options=option)
    yield driver
    driver.quit()
