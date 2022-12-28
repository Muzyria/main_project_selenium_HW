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

    select_filter_reset = '//a[@class="filter-resetHead"]'

    select_price_slider_left = '//*[@id="trackbarprice"]/a[1]/div/div'
    select_price_slider_right = '//*[@id="trackbarprice"]/a[3]/div/div'

    select_price_input_min = '//input[@id="price[min]"]'
    select_price_input_max = '//input[@id="price[max]"]'
    select_price_button_ok = '//button[@id="submitprice"]'

    # select_button_ok = '//button[@class="bluebtn"]'

    # Getters

    def get_producer_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_producer_show_all)))

    def get_producer_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_producer_list_all)))

    def get_filter_reset(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_filter_reset)))

    # PRICE
    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    def get_price_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_right)))

    def get_price_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_button_ok)))

    def get_price_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_min)))

    def get_price_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_max)))

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

    def click_producer_random_item(self, val):
        check_box_list = self.item_to_list(val)
        number_item = random.randint(1, len(check_box_list))
        name_item = check_box_list[number_item - 1]
        self.go_to_element_actions(self.driver.find_element(By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))).click()
        print(f'Click {name_item}')
        time.sleep(3)

    def click_filter_reset(self):
        self.get_filter_reset().click()
        print('Click filter RESET')

    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_price_slider_right(self):
        self.slider_right(self.select_price_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по цене

    def input_price_input_min(self):
        value = random.randint(200, 1000)
        self.get_price_input_min().clear()
        self.get_price_input_min().send_keys(value)
        print(f'input_price_input_min {value}')

    def input_price_input_max(self):
        value = random.randint(10000, 28000)
        self.get_price_input_max().clear()
        self.get_price_input_max().send_keys(value)
        print(f'input_price_input_max {value}')

    # Methods

    def run_configurator_list_spinning(self):
        self.get_current_url()
        self.click_producer_show_all()
        self.print_producer_list_all(self.get_producer_list_all())

        self.click_producer_random_item(self.get_producer_list_all())

        self.click_filter_reset()

        self.move_price_slider_left()
        self.move_price_slider_right()
        self.click_price_button_ok()
        # self.input_price_input_min()
        # self.input_price_input_max()
        # self.click_price_button_ok()

        time.sleep(3)



