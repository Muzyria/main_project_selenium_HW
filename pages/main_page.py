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

    select_pc_config = '//a[@id="out-link-5"]'

    # Getters

    def get_pc_config(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pc_config)))

    # Actions

    def click_cp_config(self):
        self.get_pc_config().click()
        print('Click link mobile')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_cp_config()








