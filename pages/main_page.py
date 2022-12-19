import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://elmir.ua/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_pc_configurator = '//a[@id="out-link-5"]'
    select_tip_button_skip = '//b[@class="dg-btn dg-skip"]'

    # Getters

    def get_pc_configurator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pc_configurator)))

    def get_tip_button_skip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_tip_button_skip)))

    # Actions

    def click_pc_configurator(self):
        self.get_pc_configurator().click()
        print('Click pc configurator')

    def click_tip_button_skip(self):
        self.get_tip_button_skip().click()
        print('Click tip button skip')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_pc_configurator()
        self.click_tip_button_skip()







