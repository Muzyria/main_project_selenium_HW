import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class CPU_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_cpu_list = '//div[@data-id="10000"]'
    select_price_slider_left = '//span[@class="ui-slider-handle ui-corner-all ui-state-default"]'

    select_price_input_min = '//input[@id="f-price-l"]'
    select_price_input_max = '//input[@id="f-price-h"]'
    select_price_button_ok = '//*[@id="price-diap"]/div[3]/button'

    # Getters

    def get_cpu_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cpu_list)))

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    def get_price_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_button_ok)))

    def get_price_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_min)))

    def get_price_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_max)))

    # Actions

    def click_cpu_list(self):
        self.get_cpu_list().click()
        print('Click CPU list')  # Открываеем список процессоров

    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по цене

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

    def open_cpu_list(self):
        self.get_current_url()
        self.click_cpu_list()
        self.move_price_slider_left()
        self.input_price_input_min()
        self.input_price_input_max()
        self.click_price_button_ok()



