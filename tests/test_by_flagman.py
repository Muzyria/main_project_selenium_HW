import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from base.base_class import Base
from pages.checkout_page import Checkout_page
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
    spin.run_price_configurator()
    spin.run_length_configurator()
    spin.run_minimum_tes_t_configurator()
    spin.run_maximum_tes_t_configurator()

    spin.run_add_to_cart()

    check = Checkout_page(driver)
    check.run_checkout_page()

    ba = Base(driver)

    ba.assert_title_cart(spin.cart_list[0], check.checkout_list[0])
    ba.assert_total_cart(spin.cart_list[1], check.checkout_list[1])

    check.run_ordering()

    time.sleep(10)
    driver.quit()
