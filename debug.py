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
        # self.base_url = 'https://elmir.ua/configurator/'
        self.base_url = 'https://www.dns-shop.ru/catalog/17a8a01d16404e77/smartfony/'
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def select_product(self):

        print('Start test')



        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                         '/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[6]/div/div/div[2]')))

        ActionChains(self.driver).move_to_element(element).perform()

        # for item in item_list:
        #
        #     print(item.text)
        # print('Prin List 1')




        ''''+++++++++++++++++'''

test = NoTest1()
test.select_product()

time.sleep(2)

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





