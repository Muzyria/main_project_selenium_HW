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
    select_list_items_cpu = '//div[@class="scrl-blu cat-products"]'  # list CPU

    # Getters

    def get_cpu_list_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cpu_list_link)))

    def get_list_items_cpu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_list_items_cpu)))
    #
    # def get_subscribe_close(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_subscribe_close)))

    # Actions

    def click_cpu_list_link(self):
        self.get_cpu_list_link().click()
        print('Click cpu list link')

    def pull_list_items_cpu(self):
        self.get_cpu_list_link().click()
        print('Click cpu list link')

    # Methods

    def open_cpu_list_link(self):
        self.get_current_url()
        self.click_cpu_list_link()
        print(self.pull_list_items_cpu().value())
