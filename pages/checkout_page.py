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

    select_total_checkout = '//td[@class="g-l-info-i g-l-info-price"]'
    select_title_checkout = '//a[@class="cart-g-l-i-title-link"]'

    select_input_phone = '//input[@name="login"]'
    select_input_first_name = '//input[@name="first_name"]'
    select_input_index = '//input[@name="index"]'
    select_input_street = '//input[@name="street"]'
    select_input_house = '//input[@name="house"]'
    select_input_flat = '//input[@name="flat"]'
    select_input_comment = '//input[@name="comment"]'

    select_check_box_custom = '//span[@class="checkbox-custom"]'

    # Getters

    def get_total_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_total_checkout)))

    def get_title_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_title_checkout)))

    def get_input_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_phone)))

    def get_input_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_first_name)))

    def get_input_index(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_index)))

    def get_input_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_street)))

    def get_input_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_house)))

    def get_input_flat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_flat)))

    def get_input_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_input_comment)))

    def get_check_box_custom(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_check_box_custom)))

    # Actions

    def input_phone(self):
        self.get_input_phone().send_keys("31234567890")
        print('Input Phone')

    def input_first_name(self):
        self.get_input_first_name().send_keys("Иванов Иван")
        print('input_first_nam')

    def input_index(self):
        self.get_input_index().send_keys("12345")
        print('Input index')

    def input_street(self):
        self.get_input_street().send_keys("Абрикосовая")
        print('Input street')

    def input_house(self):
        self.get_input_house().send_keys("100")
        print('Input House')

    def input_flat(self):
        self.get_input_flat().send_keys("10")
        print('Input Flat')

    def input_comment(self):
        self.get_input_comment().send_keys("Все хорошо !")
        print('Input Comment')

    def click_check_box_custom(self):
        self.get_check_box_custom().click()
        print('Click Check Box Custom')

    # Methods

    def run_checkout_page(self):
        self.get_current_url()
        self.checkout_list.append(self.get_title_checkout().text)
        self.checkout_list.append(self.get_total_checkout().text)

    def run_ordering(self):
        self.input_phone()
        self.input_first_name()
        self.input_index()
        self.input_street()
        self.input_house()
        self.input_flat()
        self.input_comment()
        self.click_check_box_custom()
