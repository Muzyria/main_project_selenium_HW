import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.cpu_page import CPU_page
from pages.main_page import Main_page


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page(driver)
    mp.open_main_page()

    cpu = CPU_page(driver)
    cpu.open_cpu_list()

    time.sleep(5)
    driver.quit()
