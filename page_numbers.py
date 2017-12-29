import time
import selenium_methods


URL = 'https://www.mango-office.ru/shop/numbers/'
SELECT_RANDOM_NUMBER = '/html/body/main/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/a'
CART = '/html/body/main/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[4]'
REGULAR_PRICE = '/html/body/main/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/p/small/span[1]/strong'
CONNECTION_PRICE = '/html/body/main/div[2]/div[2]/div/div[3]/div[1]/div[1]/div[4]/div[1]/p/small/span[2]/strong'
CART_ONE_TIME_PAYMENT = '/html/body/main/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[10]/span[1]'
CART_MONTHLY_PAYMENT = '/html/body/main/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[10]/span[2]'
CART_NUMBERS = '/html/body/main/div[2]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[2]/div[4]/div'


class PageNumbers(object):

    def __init__(self, driver):
        self.driver = driver
        self.page = driver.get(URL)
        self.connection_price = int(selenium_methods.find_element_by_xpath(driver, CONNECTION_PRICE).text.replace(' ', ''))
        self.regular_price = int(selenium_methods.find_element_by_xpath(driver, REGULAR_PRICE).text.replace(' ', ''))
        self.cart = PageNumbers.Cart(self.driver)

    def select_random_numbers(self, numbers_count=1):
        for i in range(numbers_count):
            selenium_methods.click(self.driver, SELECT_RANDOM_NUMBER)
            time.sleep(2)

    class Cart(object):
        def __init__(self, driver):
            self.driver = driver

        @property
        def monthly_payment(self):
            return int(selenium_methods.find_element_by_xpath(self.driver, CART_MONTHLY_PAYMENT).text.replace(' ', ''))

        @property
        def one_time_payment(self):
            return int(selenium_methods.find_element_by_xpath(self.driver, CART_ONE_TIME_PAYMENT).text.replace(' ', ''))

        @property
        def numbers_in_cart(self):
            return len(selenium_methods.find_elements_by_xpath(self.driver, CART_NUMBERS))
