import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page_DNS_V_2 import Main_page_DNS


def test_by_main_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    print('Start tests 1')

    mp = Main_page_DNS(driver)
    mp.open_main_page()

    # cpu = CPU_page(driver)
    # cpu.open_cpu_list()

    time.sleep(5)
    driver.quit()
