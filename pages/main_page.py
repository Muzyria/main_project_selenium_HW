import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page(Base):

    url = 'https://allo.ua/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'


    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))


    # Actions

    # def click_select_product_1(self):
    #     self.get_select_product_1().click()
    #     print('Click select product_1')


    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()



