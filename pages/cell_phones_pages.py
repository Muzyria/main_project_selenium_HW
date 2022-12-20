import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cell_phones_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_price_slider_left = '//span[@id="leftBegun_two"]'
    select_price_input_min = '//input[@id="minPrice"]'
    select_price_input_max = '//input[@id="maxPrice"]'
    select_price_button_ok = '//button[@type="submit"]'

    select_manufacturer_apple = '//input[@id="idm45757727913408"]'

    # Getters

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    def get_price_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_button_ok)))

    def get_price_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_min)))

    def get_price_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_max)))

    def get_manufacturer_apple(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_manufacturer_apple)))

    # Actions

    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def click_manufacturer_apple(self):
        self.get_manufacturer_apple().click()
        print('')

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')

    def input_price_input_min(self):
        value = random.randint(1000, 5000)
        self.get_price_input_min().clear()
        self.get_price_input_min().send_keys(value)
        print(f'input_price_input_min {value}')

    def input_price_input_max(self):
        value = random.randint(10000, 80000)
        self.get_price_input_max().clear()
        self.get_price_input_max().send_keys(value)
        print(f'input_price_input_max {value}')

    # Methods

    def open_cell_phones(self):
        self.get_current_url()
        self.move_price_slider_left()

        self.input_price_input_min()

        self.input_price_input_max()
        self.click_price_button_ok()
        # self.click_manufacturer_apple()


