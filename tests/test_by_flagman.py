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
    # spin.run_configurator_list_spinning()
    spin.run_price_configurator()
    spin.no_such_element_exception()
    spin.run_length_configurator()
    spin.no_such_element_exception()
    spin.run_minimum_tes_t_confgurator()
    spin.no_such_element_exception()
    spin.run_maximum_tes_t_configurator()
    spin.no_such_element_exception()

    time.sleep(10)
    driver.quit()
