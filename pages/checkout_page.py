import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Checkout_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_link_configurator = '//a[@id="out-link-5"]'


    # Getters

    def get_link_configurator(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_link_configurator)))


    # Actions

    def click_link_configurator(self):
        self.get_link_configurator().click()
        print('Click link_configurator')



    # Methods

    def open_main_page(self):
        self.driver.get(self.url)








