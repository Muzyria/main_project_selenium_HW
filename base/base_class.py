import datetime
import time
import random

from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import desired_capabilities
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    """Method assert word"""

    def assert_total_cart(self, total_cart, checkout_total):
        try:
            assert total_cart == checkout_total
            print('Good TOTAL CART')
        except AssertionError:
            print('ERROR TOTAL CART')

    def assert_title_cart(self, title_cart, title_checkout):
        try:
            assert title_cart == title_checkout
            print('Good TITLE CART')
        except AssertionError:
            print('ERROR TITLE CART')

    """Method screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(r'C:\Git_Muzyria\main_project_selenium_HW\screen\\' + name_screenshot)

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    """Method Slider Left to right"""

    def slider_left(self, locator):
        action = ActionChains(self.driver)
        slider = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value = random.randint(0, 50)
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'slider_left move to {value}')

    """Method Slider right to left"""

    def slider_right(self, locator):
        action = ActionChains(self.driver)
        slider = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value = random.randint(-50, 0)
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'slider_right move to {value}')

    """Method Slider Left to ZERO"""

    def slider_left_to_zero(self, locator):
        action = ActionChains(self.driver)
        slider = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value = -100
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'slider_left move to ZERO')

    """Method Slider right to MAX_VALUE"""

    def slider_right_to_max_value(self, locator):
        action = ActionChains(self.driver)
        slider = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value = 100
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'slider_right move to MAX')

    """Go to specified element"""

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    """Go to specified element ACTIONS"""

    def go_to_element_actions(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    """Element in LIST clickable """

    def element_is_clickable(self, item_name):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{item_name}"]')))


    """ITEM text to LIST"""  #  ???????????????????? ???????????? ???? ???????????????? ??????????????????

    def item_to_list(self, item_list):
        my_list = list(map(str, [i.text for i in item_list][0].split('\n')))
        return my_list

    # self.driver.execute_script("alert('Hello')")

