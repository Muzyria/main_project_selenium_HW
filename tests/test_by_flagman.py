import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page_flagman import Main_page_flagman


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page_flagman(driver)
    mp.open_main_page()

    # cpu = CPU_page(driver)
    # cpu.open_cpu_list()

    time.sleep(5)
    driver.quit()
