import time
import random

from selenium.webdriver import Keys
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

    select_type_of_rod_list_all = '//ul[@id="sort_detail_10908"]'

    select_filter_reset = '//a[@class="filter-resetHead"]'

    select_price_slider_left = '//*[@id="trackbarprice"]/a[1]/div/div'
    select_price_slider_right = '//*[@id="trackbarprice"]/a[3]/div/div'

    select_price_input_min = '//input[@id="price[min]"]'
    select_price_input_max = '//input[@id="price[max]"]'
    select_price_button_ok = '//button[@id="submitprice"]'

    select_sort_items = '/html/body/div[11]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/select'

    select_length_slider_left = '//*[@id="trackbar10625"]/a[1]/div/div'
    select_length_slider_right = '//*[@id="trackbar10625"]/a[3]/div/div'

    select_length_input_min = '//input[@id="10625[min]"]'
    select_length_input_max = '//input[@id="10625[max]"]'
    select_length_button_ok = '//button[@id="submit10625"]'

    select_minimum_test_slider_left = '//*[@id="trackbar10643"]/a[1]/div/div'
    select_minimum_test_slider_right = '//*[@id="trackbar10643"]/a[3]/div/div'

    select_minimum_test_input_min = '//input[@id="10643[min]"]'
    select_minimum_test_input_max = '//input[@id="10643[max]"]'
    select_minimum_test_button_ok = '//button[@id="submit10643"]'

    select_maximum_test_slider_left = '//*[@id="trackbar10644"]/a[1]/div/div'
    select_maximum_test_slider_right = '//*[@id="trackbar10644"]/a[3]/div/div'

    select_maximum_test_input_min = '//input[@id="10644[min]"]'
    select_maximum_test_input_max = '//input[@id="10644[max]"]'
    select_maximum_test_button_ok = '//button[@id="submit10644"]'

    # Getters

    def get_producer_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_producer_show_all)))

    def get_producer_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_producer_list_all)))

    def get_type_of_rod_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_type_of_rod_list_all)))

    def get_filter_reset(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_filter_reset)))

    # Getter PRICE
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

    # Getter LENGTH
    def get_length_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_slider_left)))

    def get_length_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_slider_right)))

    def get_length_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_button_ok)))

    def get_length_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_input_min)))

    def get_length_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_input_max)))

    # SORT
    def get_sort_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_sort_items)))


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

    def print_type_of_rod_list_all(self, val):
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print type_of_rod_list_all')

    # def click_type_of_rod_random_item(self, val):
    #     check_box_list = self.item_to_list(val)
    #     number_item = random.randint(1, len(check_box_list))
    #     name_item = check_box_list[number_item - 1]
    #     self.go_to_element_actions(self.driver.find_element(By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))
    #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))).click()
    #     print(f'Click {name_item}')
    #     time.sleep(3)

    def click_filter_reset(self):
        self.get_filter_reset().click()
        print('Click filter RESET')

    """PRICE SLIDER"""
    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_price_slider_right(self):
        self.slider_right(self.select_price_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по цене

    def input_price_input_min(self):
        value = random.randint(200, 9000)
        self.go_to_element_actions(self.get_price_input_min())
        current_min_val = self.get_price_input_min().get_attribute('value')
        time.sleep(1)
        self.get_price_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_price_input_min().send_keys(Keys.BACKSPACE)
        self.get_price_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_price_input_min {value}')

    def input_price_input_max(self):
        value = random.randint(10000, 28000)
        self.get_price_input_max().clear()
        self.go_to_element_actions(self.get_price_input_max())
        current_max_val = self.get_price_input_min().get_attribute('value')
        time.sleep(1)
        self.get_price_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_price_input_max().send_keys(Keys.BACKSPACE)
        self.get_price_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_price_input_max {value}')

    """LENGTH SLIDER"""
    def move_length_slider_left(self):
        self.slider_left(self.select_length_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_length_slider_right(self):
        self.slider_right(self.select_length_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def click_length_button_ok(self):
        self.get_length_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по длине

    def input_length_input_min(self):
        value = random.randint(1, 90)
        self.go_to_element_actions(self.get_length_input_min())
        current_min_val = self.get_length_input_min().get_attribute('value')
        time.sleep(1)
        self.get_length_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_length_input_min().send_keys(Keys.BACKSPACE)
        self.get_length_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_length_input_min {value}')

    def input_length_input_max(self):
        value = random.randint(100, 230)
        self.get_length_input_max().clear()
        self.go_to_element_actions(self.get_length_input_max())
        current_max_val = self.get_length_input_min().get_attribute('value')
        time.sleep(1)
        self.get_length_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_length_input_max().send_keys(Keys.BACKSPACE)
        self.get_length_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_length_input_max {value}')


    def click_sort_items(self):  # сортировка по цене от дешевых
        self.go_to_element_actions(self.get_sort_items())
        self.get_sort_items().click()
        print('Click sort items')
        [self.get_sort_items().send_keys(Keys.ARROW_UP) for _ in range(5)]
        self.get_sort_items().send_keys(Keys.RETURN)
        print('Click sort items по цене (от дешевых)')
        time.sleep(3)

    # Methods

    def run_configurator_list_spinning(self):
        self.get_current_url()
        self.click_producer_show_all()
        # self.print_producer_list_all(self.get_producer_list_all())

        # self.click_producer_random_item(self.get_producer_list_all())

        # self.click_filter_reset()


        # self.move_price_slider_left()
        # self.move_price_slider_right()
        # self.click_price_button_ok()

        # self.input_price_input_min()
        # self.input_price_input_max()
        # self.click_price_button_ok()
        #
        # self.click_sort_items()

        # self.print_type_of_rod_list_all(self.get_type_of_rod_list_all())

        self.move_length_slider_left()
        self.move_length_slider_right()
        self.input_length_input_min()
        self.input_length_input_max()

        self.click_length_button_ok()

        time.sleep(5)



