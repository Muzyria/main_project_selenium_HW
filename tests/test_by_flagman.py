import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page_flagman import Main_page_flagman
from pages.spinning_page import Spinning_page


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page_flagman(driver)
    mp.open_main_page()

    spin = Spinning_page(driver)
    spin.run_producer_list_configurator()
    # spin.run_price_configurator()
    # spin.run_length_configurator()
    # spin.run_minimum_tes_t_confgurator()
    # spin.run_maximum_tes_t_configurator()
    # spin.run_configurator_list_spinning()

    time.sleep(20)
    driver.quit()
