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

    select_price_slider_left = '//*[@id="price-slider"]/span[1]'
    select_price_slider_right = '//*[@id="price-slider"]/span[2]'

    select_price_input_min = '//input[@id="f-price-l"]'
    select_price_input_max = '//input[@id="f-price-h"]'
    select_price_button_ok = '//*[@id="price-diap"]/div[3]/button'

    select_button_ok = '//button[@class="bluebtn"]'

    select_item_list_manufacture = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[2]/ul'
    select_item_list_socket = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[3]/ul'
    select_item_list_model_range = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[4]/ul'
    select_item_list_intel_generation = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[5]/ul'
    select_item_list_amd_ryzen_series = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[6]/ul'
    select_item_list_total_number_of_cores = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[7]/ul'
    select_item_list_number_of_threads = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[8]/ul'
    select_item_list_max_memory_frequency = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[9]/ul'
    select_item_list_with_integrated_video_core = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[10]/ul'
    select_item_list_free_multiplier = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[11]/ul'
    select_item_list_tech_process = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[12]/ul'
    select_item_list_type_of_packaging = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[13]/ul'
    select_item_list_with_cooler_included = '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[14]/ul'

    # Getters

    def get_cpu_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cpu_list)))

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    def get_price_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_right)))

    def get_price_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_button_ok)))

    def get_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_button_ok)))

    def get_price_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_min)))

    def get_price_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_max)))

    """ Getters LISTS"""
    def get_item_list_manufacture(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_manufacture)))
    def get_item_list_socket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_socket)))
    def get_item_list_model_range(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_model_range)))
    def get_item_list_intel_generation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_intel_generation)))
    def get_item_list_amd_ryzen_series(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_amd_ryzen_series)))
    def get_item_list_total_number_of_cores(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_total_number_of_cores)))
    def get_item_list_number_of_threads(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_number_of_threads)))
    def get_item_list_max_memory_frequency(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_max_memory_frequency)))
    def get_item_list_with_integrated_video_core(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_with_integrated_video_core)))
    def get_item_list_free_multiplier(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_free_multiplier)))
    def get_item_list_tech_process(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_tech_process)))
    def get_item_list_type_of_packaging(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_type_of_packaging)))
    def get_item_list_with_cooler_included(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_item_list_with_cooler_included)))

    # Actions

    def click_cpu_list(self):
        self.get_cpu_list().click()
        print('Click CPU list')  # Открываеем список процессоров

    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_price_slider_right(self):
        self.slider_right(self.select_price_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по цене

    def click_button_ok(self):
        self.get_button_ok().click()
        print('click_price_button_ok')  # Кнопка OK

    def input_price_input_min(self):
        value = random.randint(400, 5000)
        self.get_price_input_min().clear()
        self.get_price_input_min().send_keys(value)
        print(f'input_price_input_min {value}')

    def input_price_input_max(self):
        value = random.randint(100000, 180000)
        self.get_price_input_max().clear()
        self.get_price_input_max().send_keys(value)
        print(f'input_price_input_max {value}')

    def check_box_click_run(self, *item_list):
        my_list = list(map(str, [i.text for i in item_list][0].split('\n')))
        for item in my_list:
            item_name = ' '.join(str(item).split(' ')[:-1])
            print(f'Click {item_name}')
            # element = self.driver.find_element(By.XPATH, f'//*[text()="{item_name} "]')
            element = self.element_is_clickable(item_name)
            try:
                self.go_to_element(element)
                self.element_is_clickable(item_name).click()
                time.sleep(0.3)
                # self.element_is_clickable(item_name).click()
            except Exception:
                continue


    # Methods

    def open_cpu_list(self):
        self.get_current_url()
        self.click_cpu_list()
        self.move_price_slider_left()
        self.move_price_slider_right()
        self.input_price_input_min()
        self.input_price_input_max()
        self.click_price_button_ok()

        self.check_box_click_run(self.get_item_list_manufacture())
        # self.get_item_list_manufacture().click()

        self.check_box_click_run(self.get_item_list_socket())
        # self.get_item_list_socket().click()

        self.check_box_click_run(self.get_item_list_model_range())

        self.check_box_click_run(self.get_item_list_intel_generation())

        self.check_box_click_run(self.get_item_list_amd_ryzen_series())

