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

    select_link_configurator = '//a[@id="out-link-5"]'
    select_subscribe_deny = '//div[@id="subscribe-deny"]'
    select_button_skip_tip = '//b[@class="dg-btn dg-skip"]'

    # Getters

    def get_link_configurator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_link_configurator)))

    def get_subscribe_deny(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscribe_deny)))

    def get_button_skip_tip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button_skip_tip)))

    # Actions

    def click_link_configurator(self):
        self.get_link_configurator().click()
        print('Click link_configurator')

    def click_subscribe_deny(self):
        self.get_subscribe_deny().click()
        print('Click subscribe_deny')

    def click_button_skip_tip(self):
        self.get_button_skip_tip().click()
        print('Click button_skip_tip')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_link_configurator()
        self.click_subscribe_deny()
        self.click_button_skip_tip()









