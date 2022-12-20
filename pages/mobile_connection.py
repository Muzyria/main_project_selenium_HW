import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Mobile_connection_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_subscribe_deny = '//div[@id="subscribe-deny"]'
    select_cell_phones = '//a[@href="/cell_phones/"]'

    # Getters

    def get_subscribe_deny(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscribe_deny)))

    def get_cell_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cell_phones)))

    # Actions

    def click_subscribe_deny(self):
        self.get_subscribe_deny().click()
        print('Click subscribe deny')

    def click_cell_phones(self):
        self.get_cell_phones().click()
        print('Click cell phones')

    # Methods

    def open_cell_phones(self):
        self.get_current_url()
        self.click_subscribe_deny()
        self.click_cell_phones()


