import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 30


def main(driver, ec, locator_type, locator):
    element = WebDriverWait(driver, TIMEOUT).until(ec((locator_type, locator)))
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    return element


def find_element_by_xpath(driver, xpath):
    element = main(driver, EC.presence_of_element_located, By.XPATH, xpath)
    return element


def find_elements_by_xpath(driver, xpath):
    elements = main(driver, EC.presence_of_all_elements_located, By.XPATH, xpath)
    return elements


def click(driver, xpath):
    element = find_element_by_xpath(driver, xpath)
    element.click()
