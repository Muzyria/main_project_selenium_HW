import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import Main_page
from pages.configurator_page import Configurator_page
from pages.select_cpu_pages import CPU_page


# @pytest.mark.run(order=1)
def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page(driver)
    mp.open_main_page()

    cp = Configurator_page(driver)
    cp.run_configurator()

    cpu = CPU_page(driver)
    cpu.select_cpu()

    time.sleep(5)
    driver.quit()
