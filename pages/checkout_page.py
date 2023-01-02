import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Checkout_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_list = []

    # Locators

    select_total_checkout = '//div[@id="cart_total"]'
    select_title_checkout = '//a[@class="cart-g-l-i-title-link"]'

    # Getters

    def get_total_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_total_checkout)))

    def get_title_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_title_checkout)))

    # Actions

    # def click_link_configurator(self):
    #     self.get_link_configurator().click()
    #     print('Click link_configurator')

    # Methods

    def run_checkout_page(self):
        self.get_current_url()
        self.checkout_list.append(self.get_title_checkout().text)
        self.checkout_list.append(self.get_total_checkout().text)









