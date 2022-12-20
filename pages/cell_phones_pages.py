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

    # Getters

    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    # Actions

    def move_price_slider_left(self):
        # self.slider_right(self.get_price_slider_left(), 50)
        action = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, self.select_price_slider_left)
        action.click_and_hold(slider).move_by_offset(40, 0).release().perform()
        print('Move price_slider_left')

    # Methods

    def open_cell_phones(self):
        self.get_current_url()
        self.move_price_slider_left()
        # self.click_cell_phones()

    # def change_slider_value(self):
    #     value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
    #     slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
    #     self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
    #     value_after = self.element_is_visible(self.locators.SLIDER_VALUE)
    #     return value_before, value_after.get_attribute('value')
