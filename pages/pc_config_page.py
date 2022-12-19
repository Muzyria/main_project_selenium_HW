import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Pc_config_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_cpu_list_link = '//*[text()="Процессор"]'

    # Getters

    def get_cpu_list_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cpu_list_link)))

    # def get_tip_button_skip(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_tip_button_skip)))
    #
    # def get_subscribe_close(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscribe_close)))

    # Actions

    def click_cpu_list_link(self):
        self.get_cpu_list_link().click()
        print('Click cpu list link')

    # def click_tip_button_skip(self):
    #     self.get_tip_button_skip().click()
    #     print('Click tip button skip')
    #
    # def click_subscribe_close(self):
    #     self.get_subscribe_close().click()
    #     print('Click subscribe close')

    # Methods

    def open_cpu_list_link(self):
        self.get_current_url()
        self.click_cpu_list_link()
