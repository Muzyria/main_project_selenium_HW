import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import Main_page


# @pytest.mark.run(order=1)
def test_by_product_1():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    # login = Login_page(driver)
    # login.authorization()

    mp = Main_page(driver)
    mp.open_main_page()
    #
    # cp = Cart_page(driver)
    # cp.product_confirmation()
    #
    # cip = Client_information_page(driver)
    # cip.input_information()
    #
    # pp = Payment_page(driver)
    # pp.payment()
    #
    # f = Finish_page(driver)
    # f.finish()

    time.sleep(5)
    driver.quit()



