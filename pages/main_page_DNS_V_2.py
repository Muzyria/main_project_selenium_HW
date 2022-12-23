import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Main_page_DNS(Base):

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_link_smartphones = '//*[text()="Смартфоны и фототехника"]'

    # Getters

    def get_link_smartphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_link_smartphones)))

    # Actions

    def click_link_smartphones(self):
        self.get_link_smartphones().click()
        print('Click link_smartphones')

    # Methods

    def open_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        # self.click_link_smartphones()
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 250);")  # идем вверх
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 550);")  # идем вверх
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 850);")  # идем вверх
