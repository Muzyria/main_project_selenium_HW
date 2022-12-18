import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=1)
def test_by_product_1(set_up, set_group):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.product_confirmation()

    cip = Client_information_page(driver)
    cip.input_information()

    pp = Payment_page(driver)
    pp.payment()

    f = Finish_page(driver)
    f.finish()

    # time.sleep(5)
    driver.quit()


# @pytest.mark.run(order=2)
def test_by_product_2(set_up, set_group):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 2')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # time.sleep(5)
    driver.quit()


# @pytest.mark.run(order=3)
def test_by_product_3(set_up, set_group):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 3')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.product_confirmation()

    # time.sleep(5)
    driver.quit()
