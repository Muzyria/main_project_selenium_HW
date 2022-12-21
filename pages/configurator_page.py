import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Configurator_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_subscribe_deny = '//div[@id="subscribe-deny"]'
    select_button_skip_tip = '//b[@class="dg-btn dg-skip"]'
    select_button_cpu_list = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div'

    # Getters

    def get_subscribe_deny(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscribe_deny)))

    def get_button_skip_tip(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button_skip_tip)))

    def get_button_cpu_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button_cpu_list)))

    # Actions

    def click_subscribe_deny(self):
        self.get_subscribe_deny().click()
        print('Click subscribe deny')

    def click_button_skip_tip(self):
        self.get_button_skip_tip().click()
        print('Click button skip tip')

    def click_button_cpu_list(self):
        self.get_button_cpu_list().click()
        print('Click button_cpu_list')

    # Methods

    def run_configurator(self):
        self.get_current_url()
        self.click_subscribe_deny()
        self.click_button_skip_tip()
        self.click_button_cpu_list()


