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

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

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
        value = random.randint(20, 50)
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'price_slider_left move to {value}')

    """Method Slider right to left"""

    def slider_right(self, locator):
        action = ActionChains(self.driver)
        slider = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        value = random.randint(-50, 0)
        action.click_and_hold(slider).move_by_offset(value, 0).release().perform()
        print(f'price_slider_right move to {value}')

    """Go to specified element"""

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 50", element)

    """Go to specified element ACTIONS"""

    def go_to_element_actions(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    """Element in LIST clickable """

    def element_is_clickable(self, item_name):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{item_name}"]')))



