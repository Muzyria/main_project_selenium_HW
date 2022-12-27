import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Spinning_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_producer_show_all = '//span[text()="Показать еще..."]'
    select_producer_list_all = '//ul[@id="sort_producer"]'

    # Getters

    def get_producer_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_producer_show_all)))

    def get_producer_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_producer_list_all)))



    # Actions

    def click_producer_show_all(self):
        self.get_producer_show_all().click()
        print('Click manufacturer_show_all')

    def print_producer_list_all(self, val):
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print producer_list_all')

    def check_box_click_run(self, *item_list):
        my_list = list(map(str, [i.text for i in item_list][0].split('\n')))
        count = 5
        # for item in my_list:
        for _ in range(5):
            item = my_list[random.randint(0, len(my_list) - 1)]
            item_name = item[:item.index('(')] if '(' in item else item
            print(f'Click {item_name}')



    # Methods

    def run_configurator_list_spinning(self):
        self.get_current_url()
        self.click_producer_show_all()
        self.print_producer_list_all(self.get_producer_list_all())
        # self.check_box_click_run(self.get_producer_list_all())



