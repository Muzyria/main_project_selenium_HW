import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


from pages.main_page import Main_page
from pages.pc_config_page import Pc_config_page


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page(driver)
    mp.open_main_page()

    pc_config = Pc_config_page(driver)
    pc_config.open_cpu_list_link()

    time.sleep(10)
    driver.quit()
