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

    select_language_ru = '//span[@class="mh-lang__item"]'
    select_location = '//div[@class="mh-loc"]'
    select_city_lviv = 'href="https://allo.ua/ru/l-viv/"'


    # Getters

    def get_select_language_ru(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_language_ru)))

    def get_select_location(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_location)))

    def get_select_city_lviv(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_city_lviv)))

    # Actions

    def click_select_language_ru(self):
        self.get_select_language_ru().click()
        print('Click select language RU')

    def click_select_location(self):
        self.get_select_location().click()
        print('Click select location')

    def click_select_city_lviv(self):
        self.get_select_city_lviv().click()
        print('Click select city lviv')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        # self.click_select_language_ru()

        # self.dismiss_alert()
        # self.click_select_location()
        # self.click_select_city_lviv()
        self.dismiss_alert()





