import time
import random


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from base.base_class import Base


class NoTest1(Base):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.base_url = 'https://demoqa.com/checkbox'
        self.base_url = 'https://elmir.ua/configurator/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def select_product(self):

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

        item_list2 = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                         '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[2]/ul')))
        # for item in item_list:
        #
        #     print(item.text)
        # print('Prin List 1')


        # item_list_3 = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH,
        #                                                                  '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[4]/ul')))
        #
        #
        #
        # my_list = list(map(str, [i.text for i in item_list_3][0].split('\n')))
        #
        # for item in my_list:
        #     item_name = ' '.join(str(item).split(' ')[:-1])
        #     print(item_name)
        #
        #     element = self.driver.find_element(By.XPATH, f'//*[text()="{item_name} "]')
        #     try:
        #         # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        #         self.go_to_element(element)
        #     # actions = ActionChains(self.driver)
        #     # actions.move_to_element(element).perform()
        #     #     WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[text()="{item_name} "]'))).click()
        #         self.element_is_clickable(item_name).click()
        #         time.sleep(0.3)
        #     except Exception:
        #         continue
        print('Prin List 3 --------------------------------')

        ''''-----------------------'''
    def get_val(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="cnf-content"]/div/div/div[4]/div[2]/div[1]/div[2]/aside/form/div[4]/ul')))

    def check_box_click_run(self):
        my_list = list(map(str, [i.text for i in self.get_val()][0].split('\n')))
        for item in my_list:
            print(item)
            # item_name = ' '.join(str(item).split(' ')[:-1])
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
            element = self.driver.find_element(By.XPATH, f'//*[text()="{item_name}"]')
            try:
                self.go_to_element(element)
                self.element_is_clickable(item_name).click()
                time.sleep(0.5)
            except Exception:
                continue




        ''''+++++++++++++++++'''

test = NoTest1()
test.select_product()
# test.click_random_checkbox()
time.sleep(2)
test.check_box_click_run()
test.driver.close()


# def click_random_checkbox(self):
#     item_list = self.elements_are_visible(self.locators.ITEM_LIST)
#     count = 21
#     while count != 0:
#         item = item_list[random.randint(1, 15)]
#         if count > 0:
#             self.go_to_element(item)
#             item.click()
#             # time.sleep(0.5)
#             count -= 1
#         else:
#             break


# EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
# ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
# CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
# TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
# OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")




