import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Spinning_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_manufacturer_show_all = '//span[text()="Показать еще..."]'

    # Getters

    def get_manufacturer_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_manufacturer_show_all)))

    # Actions

    def click_manufacturer_show_all(self):
        self.get_manufacturer_show_all().click()
        print('Click manufacturer_show_all')

    # Methods

    def run_configurator_list_spinning(self):
        self.get_current_url()
        self.click_manufacturer_show_all()



