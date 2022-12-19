import datetime

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.alert import Alert


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

    """Method dismiss alert"""

    def dismiss_alert(self):
        try:
            # switch to alert and click ok button
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            print("exception hanlded")





