import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.common.exceptions import NoSuchElementException

class Spinning_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.cart_list = []

    # Locators

    """CHECKBOXES"""
    select_producer_show_all = '//span[text()="Показать еще..."]'
    select_producer_list_all = '//ul[@id="sort_producer"]'
    select_type_of_rod_list_all = '//ul[@id="sort_detail_10908"]'
    select_type_of_rod_first_item = '/html/body/div[11]/div[3]/div/div[2]/div[1]/form/div[2]/div[5]/ul/li[1]/label/span[1]'
    select_number_of_sections_list_all = '//ul[@id="sort_10627"]'
    select_line_up_action_list_all = '//ul[@id="sort_10631"]'
    select_form_material_list_all = '//ul[@id="sort_10626"]'
    select_handle_material_list_all = '//ul[@id="sort_10628"]'
    select_tip_type_list_all = '//ul[@id="sort_10660"]'

    # Сброс фильтра
    select_filter_reset = '//a[@class="filter-resetHead"]'

    """CART BUTTON AND MENU"""
    select_cart_button_first = '//a[@name="topurchases"]'

    select_continue_shopping_button = '//*[@id="continue-shopping"]'
    select_product_name_for_add_cart = '//*[@id="cart_item1"]/div/div[2]/div'
    select_product_total_cart = '//span[@id="cart_total"]'
    select_checkout_button = '//button[@class="checkout-btn btn red-btn floatRight"]'
    #

    """RETURN TO spiinning page"""
    select_return_to_spinning_page = '/html/body/div[11]/div[2]/div/div[1]/nav/ul/li[2]/a/span'
    select_return_to_spinning_page_2 = '/html/body/div[12]/div[2]/div/div[1]/nav/ul/li[2]/a'

    """PRICE SLIDER and INPUT"""
    select_price_slider_left = '//*[@id="trackbarprice"]/a[1]/div/div'
    select_price_slider_right = '//*[@id="trackbarprice"]/a[3]/div/div'
    select_price_input_min = '//input[@id="price[min]"]'
    select_price_input_max = '//input[@id="price[max]"]'
    select_price_button_ok = '//button[@id="submitprice"]'

    """LIST of SORT"""
    select_sort_items = '/html/body/div[11]/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/select'

    """LENGTH SLIDER and INPUT"""
    select_length_slider_left = '//*[@id="trackbar10625"]/a[1]/div/div'
    select_length_slider_right = '//*[@id="trackbar10625"]/a[3]/div/div'
    select_length_input_min = '//input[@id="10625[min]"]'
    select_length_input_max = '//input[@id="10625[max]"]'
    select_length_button_ok = '//button[@id="submit10625"]'

    """MINIMUM TEST SLIDER and INPUT"""
    select_minimum_test_slider_left = '//*[@id="trackbar10643"]/a[1]/div/div'
    select_minimum_test_slider_right = '//*[@id="trackbar10643"]/a[3]/div/div'
    select_minimum_test_input_min = '//input[@id="10643[min]"]'
    select_minimum_test_input_max = '//input[@id="10643[max]"]'
    select_minimum_test_button_ok = '//button[@id="submit10643"]'

    """MAXIMUM TEST SLIDER and INPUT"""
    select_maximum_test_slider_left = '//*[@id="trackbar10644"]/a[1]/div/div'
    select_maximum_test_slider_right = '//*[@id="trackbar10644"]/a[3]/div/div'
    select_maximum_test_input_min = '//input[@id="10644[min]"]'
    select_maximum_test_input_max = '//input[@id="10644[max]"]'
    select_maximum_test_button_ok = '//button[@id="submit10644"]'

    # Getters

    """checkboxes"""
    def get_producer_show_all(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_producer_show_all)))

    def get_producer_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_producer_list_all)))

    def get_type_of_rod_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_type_of_rod_list_all)))

    def get_number_of_sections_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_number_of_sections_list_all)))

    def get_line_up_action_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_line_up_action_list_all)))

    def get_form_material_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_form_material_list_all)))

    def get_handle_material_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_handle_material_list_all)))

    def get_tip_type_list_all(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.select_tip_type_list_all)))
    """"""

    def get_filter_reset(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_filter_reset)))

    def get_return_to_spinning_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_return_to_spinning_page)))

    def get_return_to_spinning_page_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_return_to_spinning_page_2)))

    """CART and menu"""
    def get_cart_button_first(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart_button_first)))

    def get_continue_shopping_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_continue_shopping_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_checkout_button)))

    def get_product_name_for_add_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_name_for_add_cart)))

    def get_product_total_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_total_cart)))

    # Getter PRICE
    def get_price_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_left)))

    def get_price_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_slider_right)))

    def get_price_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_button_ok)))

    def get_price_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_min)))

    def get_price_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_price_input_max)))

    # Getter LENGTH
    def get_length_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_slider_left)))

    def get_length_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_slider_right)))

    def get_length_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_button_ok)))

    def get_length_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_input_min)))

    def get_length_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_length_input_max)))

    # Getter minimum_test
    def get_minimum_tes_t_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_minimum_test_slider_left)))

    def get_minimum_tes_t_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_minimum_test_slider_right)))

    def get_minimum_tes_t_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_minimum_test_button_ok)))

    def get_minimum_tes_t_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_minimum_test_input_min)))

    def get_minimum_tes_t_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_minimum_test_input_max)))

    # Getter maximum_test
    def get_maximum_tes_t_slider_left(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_maximum_test_slider_left)))

    def get_maximum_tes_t_slide_right(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_maximum_test_slider_right)))

    def get_maximum_tes_t_button_ok(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_maximum_test_button_ok)))

    def get_maximum_tes_t_input_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_maximum_test_input_min)))

    def get_maximum_tes_t_input_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_maximum_test_input_max)))

    # SORT
    def get_sort_items(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_sort_items)))

    # Actions

    def no_such_element_exception(self):
        """Проверка на отсуцтвие результатов фильтра"""
        try:
            self.driver.find_element(By.XPATH, '//div[@class="alert alert-warning"]')
            print('Не получилось ни чего выбрать, пробуем снова !')
            return True
        except NoSuchElementException:
            print('Пока все в норме продолжаем тест')
            return False

    def no_such_cart_button_exception(self):
        """Проверка на отсуцтвие кнопки добавить в корзину"""
        try:
            self.driver.find_element(By.XPATH, self.select_cart_button_first)
            print('Кнопка добавить в корзину есть продолжаем тест')
            return True
        except NoSuchElementException:
            print('Нет кнопки добавить в корзину!')
            return False

    def click_producer_show_all(self):
        """Кнопка развернуть показать все в блоке производителей"""
        try:
            self.get_producer_show_all().click()
            print('Click manufacturer_show_all')
        except Exception:
            print('Нет кнопки развернуть список')

    def print_producer_list_all(self, val):
        """Вывести в консоль список производителей"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            # print(item_name)
        print('Print producer_list_all')

    def click_producer_random_item(self, val):
        """Выбор рандомного производителя и выбор его"""
        check_box_list = self.item_to_list(val)
        number_item = random.randint(1, len(check_box_list))
        name_item = check_box_list[number_item - 1]
        print(f'random select {name_item} and try click {number_item}')
        self.go_to_element_actions(self.driver.find_element(By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="sort_producer"]/li[{number_item}]'))).click()
        print(f'Click {name_item}')
        time.sleep(3)

    def click_type_of_rod_first_item(self):
        """Выбор первого пункта в блоке тип удилища"""
        try:
            self.go_to_element_actions(self.driver.find_element(By.XPATH, self.select_type_of_rod_list_all))
            # self.go_to_element_actions(self.driver.find_element(By.XPATH, self.select_type_of_rod_first_item))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_type_of_rod_first_item))).click()
        except Exception:
            print('Не найден блок тип удилища')

    def print_type_of_rod_list_all(self, val):
        """Вывести в консоль список типов удилища"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print type_of_rod_list_all')

    def print_number_of_sections_list_all(self, val):
        """Вывести в консоль список блока количества секций"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print number_of_sections_list_all')

    def print_line_up_action_list_all(self, val):
        """Вывести в консоль список блока строй удилища"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print line_up_action_list_all')

    def print_form_material_list_all(self, val):
        """Вывести в консоль список блока материал бланка"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print form_material_list_all')

    def print_handle_material_list_all(self, val):
        """Вывести в консоль список блока материал рукоятки"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print handle_material_list_all')

    def print_tip_type_list_all(self, val):
        """Вывести в консоль список блокаа тип вершинки"""
        print(self.item_to_list(val))
        for item in self.item_to_list(val):
            item_name = item[:item.index('(')] if '(' in item else item
            print(item_name)
        print('Print tip_type_list_all')

    def click_filter_reset(self):
        """Сброс фильтра"""
        self.get_filter_reset().click()
        print('Click filter RESET')

    """CART and menu"""
    def click_cart_button_first(self):
        try:
            self.go_to_element_actions(self.get_cart_button_first())
            time.sleep(2)
            self.get_cart_button_first().click()
            print('Click cart_button_first')
            self.print_product_name_for_add_cart()
            self.print_product_total_cart()
            time.sleep(3)
        except Exception:
            print('Что то пошло не так. и не нашло кнопку корзины')

    def click_continue_shopping_button(self):
        self.get_continue_shopping_button().click()
        print('Click continue_shopping_button')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout_button')

    def print_product_name_for_add_cart(self):
        name_product = self.get_product_name_for_add_cart().text
        self.cart_list.append(name_product)
        print(f'name_product {name_product}')

    def print_product_total_cart(self):
        total_product = self.get_product_total_cart().text
        self.cart_list.append(total_product)
        print(f'Total_product {total_product}')

    def click_return_to_spinning_page(self):
        try:
            self.get_return_to_spinning_page().click()
            print('Click return_to_spinning_page')
        except Exception:
            self.get_return_to_spinning_page_2().click()
            print('Click return_to_spinning_page_2')

    """PRICE SLIDER"""
    def move_price_slider_left(self):
        self.slider_left(self.select_price_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_price_slider_right(self):
        self.slider_right(self.select_price_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def move_price_slider_left_zero(self):
        self.slider_left_to_zero(self.select_price_slider_left)  # Левый слайдер двигаем to ZERO%

    def move_price_slider_right_max(self):
        self.slider_right_to_max_value(self.select_price_slider_right)  # Правый слайдер двигаем to MAX%

    def click_price_button_ok(self):
        self.get_price_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по цене

    def input_price_input_min(self):
        # value = random.randint(200, 9000)
        self.go_to_element_actions(self.get_price_input_min())
        current_min_val = int(self.get_price_input_min().get_attribute('value'))
        current_max_val = int(self.get_price_input_max().get_attribute('value'))
        value = random.randint(current_min_val, current_min_val + int(current_max_val / 10))
        time.sleep(1)
        self.get_price_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_price_input_min().send_keys(Keys.BACKSPACE)
        self.get_price_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_price_input_min {value}')

    def input_price_input_max(self):
        # value = random.randint(10000, 28000)
        self.get_price_input_max().clear()
        self.go_to_element_actions(self.get_price_input_max())
        current_min_val = int(self.get_price_input_min().get_attribute('value'))
        current_max_val = int(self.get_price_input_max().get_attribute('value'))
        value = random.randint(current_max_val - int(current_max_val / 10), current_max_val)
        time.sleep(1)
        self.get_price_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_price_input_max().send_keys(Keys.BACKSPACE)
        self.get_price_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_price_input_max {value}')
    # -------------------------------------------------------------------

    """LENGTH SLIDER"""
    def move_length_slider_left(self):
        self.slider_left(self.select_length_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_length_slider_right(self):
        self.slider_right(self.select_length_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def move_length_slider_left_zero(self):
        self.slider_left_to_zero(self.select_length_slider_left)  # Левый слайдер двигаем to ZERO%

    def move_length_slider_right_max(self):
        self.slider_right_to_max_value(self.select_length_slider_right)  # Правый слайдер двигаем to MAX%

    def click_length_button_ok(self):
        self.get_length_button_ok().click()
        print('click_price_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по длине

    def input_length_input_min(self):
        # value = random.randint(1, 90)
        self.go_to_element_actions(self.get_length_input_min())
        current_min_val = float(self.get_length_input_min().get_attribute('value'))
        current_max_val = float(self.get_length_input_max().get_attribute('value'))
        value = round(random.uniform(current_min_val, round(current_min_val + float(current_max_val / 10), 2)), 2)
        time.sleep(1)
        self.get_length_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_length_input_min().send_keys(Keys.BACKSPACE)
        self.get_length_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_length_input_min {value}')

    def input_length_input_max(self):
        # value = random.randint(100, 230)
        self.get_length_input_max().clear()
        self.go_to_element_actions(self.get_length_input_max())
        current_min_val = float(self.get_length_input_min().get_attribute('value'))
        current_max_val = float(self.get_length_input_max().get_attribute('value'))
        value = round(random.uniform(round(current_max_val - float(current_max_val / 10), 2), current_max_val), 2)
        time.sleep(1)
        self.get_length_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_length_input_max().send_keys(Keys.BACKSPACE)
        self.get_length_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_length_input_max {value}')
    # ------------------------------------------------------------------------------

    """MINIMUM TEST SLIDER"""

    def move_minimum_tes_t_slider_left(self):
        self.slider_left(self.select_minimum_test_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_minimum_tes_t_slider_right(self):
        self.slider_right(self.select_minimum_test_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def move_minimum_tes_t_slider_left_zero(self):
        self.slider_left_to_zero(self.select_minimum_test_slider_left)  # Левый слайдер двигаем to ZERO%

    def move_minimum_tes_t_slider_right_max(self):
        self.slider_right_to_max_value(self.select_minimum_test_slider_right)  # Правый слайдер двигаем to MAX%

    def click_minimum_tes_t_button_ok(self):
        self.get_minimum_tes_t_button_ok().click()
        print('click_minimum_tes_t_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по минитальному тесту

    def input_minimum_tes_t_input_min(self):
        # value = random.randint(0, 300)
        self.go_to_element_actions(self.get_minimum_tes_t_input_min())
        current_min_val = int(self.get_minimum_tes_t_input_min().get_attribute('value'))
        current_max_val = int(self.get_minimum_tes_t_input_max().get_attribute('value'))
        value = random.randint(current_min_val, current_min_val + int(current_max_val / 10))
        time.sleep(1)
        self.get_minimum_tes_t_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_minimum_tes_t_input_min().send_keys(Keys.BACKSPACE)
        self.get_minimum_tes_t_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_minimum_tes_t_input_min {value}')

    def input_minimum_tes_t_input_max(self):
        # value = random.randint(400, 800)
        self.get_minimum_tes_t_input_max().clear()
        self.go_to_element_actions(self.get_minimum_tes_t_input_max())
        current_min_val = int(self.get_minimum_tes_t_input_min().get_attribute('value'))
        current_max_val = int(self.get_minimum_tes_t_input_max().get_attribute('value'))
        value = random.randint(current_max_val - int(current_max_val / 10), current_max_val)
        time.sleep(1)
        self.get_minimum_tes_t_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_minimum_tes_t_input_max().send_keys(Keys.BACKSPACE)
        self.get_minimum_tes_t_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_minimum_tes_t_input_max {value}')

    # ------------------------------------------------------------------------------

    """MAXIMUM TEST SLIDER"""

    def move_maximum_tes_t_slider_left(self):
        self.slider_left(self.select_maximum_test_slider_left)  # Левый слайдер двигаем в право рандомно от 0 до 50%

    def move_maximum_tes_t_slider_right(self):
        self.slider_right(self.select_maximum_test_slider_right)  # Правый слайдер двигаем в лево рандомно от 0 до 50%

    def move_maximum_tes_t_slider_left_zero(self):
        self.slider_left_to_zero(self.select_maximum_test_slider_left)  # Левый слайдер двигаем to ZERO%

    def move_maximum_tes_t_slider_right_max(self):
        self.slider_right_to_max_value(self.select_maximum_test_slider_right)  # Правый слайдер двигаем to MAX%

    def click_maximum_tes_t_button_ok(self):
        self.get_maximum_tes_t_button_ok().click()
        print('click_maximum_tes_t_button_ok')  # Кнопка ПРИМЕНИТЬ фильтр по максимальному тесту

    def input_maximum_tes_t_input_min(self):
        # value = random.randint(1, 300)
        self.go_to_element_actions(self.get_maximum_tes_t_input_min())
        current_min_val = int(self.get_maximum_tes_t_input_min().get_attribute('value'))
        current_max_val = int(self.get_maximum_tes_t_input_max().get_attribute('value'))
        value = random.randint(current_min_val, current_min_val + int(current_max_val / 10))
        time.sleep(1)
        self.get_maximum_tes_t_input_min().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_maximum_tes_t_input_min().send_keys(Keys.BACKSPACE)
        self.get_maximum_tes_t_input_min().send_keys(value)
        # time.sleep(3)
        print(f'input_maximum_tes_t_input_min {value}')

    def input_maximum_tes_t_input_max(self):
        # value = random.randint(350, 600)
        self.get_maximum_tes_t_input_max().clear()
        self.go_to_element_actions(self.get_maximum_tes_t_input_max())
        current_min_val = int(self.get_maximum_tes_t_input_min().get_attribute('value'))
        current_max_val = int(self.get_maximum_tes_t_input_max().get_attribute('value'))
        value = random.randint(current_max_val - int(current_max_val / 10), current_max_val)
        time.sleep(1)
        self.get_maximum_tes_t_input_max().send_keys(Keys.ARROW_DOWN)
        for _ in range(8):
            self.get_maximum_tes_t_input_max().send_keys(Keys.BACKSPACE)
        self.get_maximum_tes_t_input_max().send_keys(value)
        # time.sleep(3)
        print(f'input_maximum_tes_t_input_max {value}')

    # ------------------------------------------------------------------------------

    def click_sort_items(self):
        """сортировка по цене от дешевых"""
        self.go_to_element_actions(self.get_sort_items())
        self.get_sort_items().click()
        print('Click sort items')
        [self.get_sort_items().send_keys(Keys.ARROW_UP) for _ in range(5)]
        self.get_sort_items().send_keys(Keys.RETURN)
        print('Click sort items по цене (от дешевых)')
        time.sleep(3)

    # Methods

    def run_producer_list_configurator(self):
        """Блок выбора производителя"""
        while True:
            self.get_current_url()
            self.click_producer_show_all()
            self.print_producer_list_all(self.get_producer_list_all())
            self.click_producer_random_item(self.get_producer_list_all())
            if self.no_such_cart_button_exception():
                print('Кнопка добавить в корзину есть, продолжаем вибирать !')
                break
            else:
                print('Нет кнопки добавить в корзину, пробуем повторить поиск')
                self.click_filter_reset()
                time.sleep(5)
                continue

    def run_type_of_rod_configurator(self):
        """Блок выбора типа удилища"""
        while True:
            self.print_type_of_rod_list_all(self.get_type_of_rod_list_all())
            self.click_type_of_rod_first_item()
            if self.no_such_cart_button_exception():
                print('Выбран тип удилища !')
                break
            else:
                print('Нет ')
                time.sleep(5)
                continue

    def run_price_configurator(self):
        """"слайдер выбора по цене"""
        self.move_price_slider_left()
        self.move_price_slider_right()
        self.input_price_input_min()
        self.input_price_input_max()
        self.click_price_button_ok()
        # if self.no_such_element_exception():
        if not self.no_such_cart_button_exception():
            print('Не получилось выбрать возвращаем цену назад')
            self.move_price_slider_left_zero()
            self.move_price_slider_right_max()
            self.click_price_button_ok()
        else:
            print('SELECT PRICE OK !')

    def run_length_configurator(self):
        """слайдер выбора по длине"""
        self.move_length_slider_left()
        self.move_length_slider_right()
        self.input_length_input_min()
        self.input_length_input_max()
        self.click_length_button_ok()
        # if self.no_such_element_exception():
        if not self.no_such_cart_button_exception():
            print('Не получилось выбрать возвращаем длину назад')
            self.move_length_slider_left_zero()
            self.move_length_slider_right_max()
            self.click_length_button_ok()
        else:
            print('SELECT LENGTH OK !')

    def run_minimum_tes_t_configurator(self):
        """слайдер выбора по минимальному тесту"""
        self.move_minimum_tes_t_slider_left()
        self.move_minimum_tes_t_slider_right()
        self.input_minimum_tes_t_input_min()
        self.input_minimum_tes_t_input_max()
        self.click_minimum_tes_t_button_ok()
        # if self.no_such_element_exception():
        if not self.no_such_cart_button_exception():
            print('Не получилось выбрать возвращаем минимальный тест назад')
            self.move_minimum_tes_t_slider_left_zero()
            self.move_minimum_tes_t_slider_right_max()
            self.click_minimum_tes_t_button_ok()
        else:
            print('SELECT MINIMUM TEST OK !')

    def run_maximum_tes_t_configurator(self):
        """слайдер выбора по максимальному тесту"""
        self.move_maximum_tes_t_slider_left()
        self.move_maximum_tes_t_slider_right()
        self.input_maximum_tes_t_input_min()
        self.input_maximum_tes_t_input_max()
        self.click_maximum_tes_t_button_ok()
        # if self.no_such_element_exception():
        if not self.no_such_cart_button_exception():
            print('Не получилось выбрать возвращаем максимальный тест назад')
            self.move_maximum_tes_t_slider_left_zero()
            self.move_maximum_tes_t_slider_right_max()
            self.click_maximum_tes_t_button_ok()
        else:
            print('SELECT MAXIMUM TEST OK !')

    def run_add_to_cart(self):
        """Нажатие на кнопку корзины"""
        self.click_cart_button_first()
        self.click_checkout_button()
