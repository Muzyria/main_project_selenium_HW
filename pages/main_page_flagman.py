import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page_flagman(Base):

    url = 'https://www.flagman.kiev.ua/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_link_spinning = '//i[@class="icon icon-menu_item_2"]'

    # Getters

    def get_link_spinning(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_link_spinning)))

    # Actions

    def click_link_spinning(self):
        self.get_link_spinning().click()
        print('Click link_spinning')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_spinning()


