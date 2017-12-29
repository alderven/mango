import os
import time
import configparser
import selenium_methods

CONFIG = 'config.cfg'


class PageNumbers(object):

    def __init__(self, driver):
        self.driver = driver
        self.page = driver.get(self.config['SITE']['URL'])
        self.connection_price = int(selenium_methods.find_element_by_xpath(driver, self.config['LOCATORS']['CONNECTION_PRICE']).text.replace(' ', ''))
        self.regular_price = int(selenium_methods.find_element_by_xpath(driver, self.config['LOCATORS']['REGULAR_PRICE']).text.replace(' ', ''))
        self.cart = PageNumbers.Cart(self.driver, self.config)

    @property
    def config(self):
        cfg = configparser.ConfigParser()
        cfg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG)
        cfg.read(cfg_path)
        return cfg

    def select_random_numbers(self, numbers_count=1):
        for i in range(numbers_count):
            selenium_methods.click(self.driver, self.config['LOCATORS']['SELECT_RANDOM_NUMBER'])
            time.sleep(2)

    class Cart(object):
        def __init__(self, driver, config):
            self.driver = driver
            self.config = config

        @property
        def monthly_payment(self):
            return int(selenium_methods.find_element_by_xpath(self.driver, self.config['LOCATORS']['CART_MONTHLY_PAYMENT']).text.replace(' ', ''))

        @property
        def one_time_payment(self):
            return int(selenium_methods.find_element_by_xpath(self.driver, self.config['LOCATORS']['CART_ONE_TIME_PAYMENT']).text.replace(' ', ''))

        @property
        def numbers_in_cart(self):
            return len(selenium_methods.find_elements_by_xpath(self.driver, self.config['LOCATORS']['CART_NUMBERS']))
