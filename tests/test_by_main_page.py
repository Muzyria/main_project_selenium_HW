import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.cell_phones_pages import Cell_phones_page
from pages.main_page import Main_page
from pages.mobile_connection import Mobile_connection_page


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page(driver)
    mp.open_main_page()

    mc = Mobile_connection_page(driver)
    mc.open_cell_phones()

    cp = Cell_phones_page(driver)
    cp.open_cell_phones()

    time.sleep(5)
    driver.quit()
