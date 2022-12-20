import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class NoTest1:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.base_url = 'https://demoqa.com/checkbox'
        self.base_url = 'https://elmir.ua/configurator/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def select_product(self):
        EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
        ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
        CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
        TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
        OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")

        print('Start test')

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//div[@id="subscribe-deny"]'))).click()

        print('Close alert')

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//b[@class="dg-btn dg-skip"]'))).click()

        print('Skip Tip')

        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div'))).click()

        print('Click CPU')

        item_list = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                         '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[2]/ul')))
        for item in item_list:
            print(item.text)
        print('Prin List 1')

        item_list_2 = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                         '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[3]/b')))
        for item in item_list_2:
            print(item.text)
        print('Prin List 1')




test = NoTest1()
test.select_product()
time.sleep(5)
test.driver.close()


# EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
# ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
# CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
# TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
# OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")




