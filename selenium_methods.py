from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30


def find_element_by_xpath(driver, xpath):
    element = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return element


def find_elements_by_xpath(driver, xpath):
    elements = WebDriverWait(driver, TIMEOUT).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    return elements


def click(driver, xpath):
    element = find_element_by_xpath(driver, xpath)
    element.click()
