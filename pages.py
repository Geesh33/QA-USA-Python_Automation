import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import retrieve_phone_code


class UrbanRoutesPage:
    # Address fields
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Tariff and call button
    supportive_plan_card = (By.XPATH, '//div[contains(text(),"Supportive")]')
    supportive_plan_card_parent = (By.XPATH, '//div[contains(text(),"Supportive")]//..')
    active_plan_card = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    call_taxi_button = (By.XPATH, '//button[contains(text(),"Call a taxi")]')

    # Phone number flow
    phone_number_control = (By.XPATH, '//div[@class="np-button"]//div[contains(text(), "Phone number")]')
    phone_number_input = (By.ID, 'phone')
    phone_number_code_input = (By.ID, 'code')
    phone_number_next_button = (By.CSS_SELECTOR, '.full')
    phone_number_confirm_button = (By.XPATH, '//button[contains(text(), "Confirm")]')
    phone_number = (By.CLASS_NAME, 'np-text')

    # Card details
    card_number_input = (By.ID, 'card-number')
    expiry_date_input = (By.ID, 'card-expiry')
    cvv_input = (By.ID, 'card-cvv')

    # Driver comment
    driver_comment_input = (By.ID, 'driver-comment')

    # Extras
    order_blanket_button = (By.ID, 'order-blanket')
    order_handkerchief_button = (By.ID, 'order-handkerchief')
    order_ice_cream_button = (By.ID, 'order-ice-cream')

    # Car model display
    car_model_id = (By.ID, 'car-model')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        from_field = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(self.from_field))
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_call_taxi_button(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.call_taxi_button))
        self.driver.find_element(*self.call_taxi_button).click()

    def set_phone(self, number):
        self.driver.find_element(*self.phone_number_control).click()
        self.driver.find_element(*self.phone_number_input).send_keys(number)
        self.driver.find_element(*self.phone_number_next_button).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.phone_number_code_input).send_keys(code)
        self.driver.find_element(*self.phone_number_confirm_button).click()

    def get_phone(self):
        return self.driver.find_element(*self.phone_number).text

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def select_supportive_plan(self):
        self.driver.find_element(*self.supportive_plan_card).click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.active_plan_card).text

    def enter_phone_number(self, phone_number):
        self.driver.find_element(self.phone_number_control).click()
        self.driver.find_element(self.phone_number_input).send_keys(phone_number)
        self.driver.find_element(self.phone_number_next_button).click()
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(self.phone_number_code_input).send_keys(code)
        self.driver.find_element(self.phone_number_confirm_button).click()

    def enter_card_details(self, number, expiry, cvv):
        self.driver.find_element(*self.card_number_input).send_keys(number)
        self.driver.find_element(*self.expiry_date_input).send_keys(expiry)
        self.driver.find_element(*self.cvv_input).send_keys(cvv)
        self.driver.find_element(*self.cvv_input).send_keys(Keys.TAB)

    def add_driver_comment(self, comment):
        comment_input = self.driver.find_element(*self.driver_comment_input)
        comment_input.clear()
        comment_input.send_keys(comment)

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.order_blanket_button).click()
        self.driver.find_element(*self.order_handkerchief_button).click()

    def order_multiple_ice_creams(self, count=1):
        for _ in range(count):
            self.driver.find_element(*self.order_ice_cream_button).click()
            time.sleep(0.2)

    def car_model_is_visible(self):
        try:
            return self.driver.find_element(*self.car_model_id).is_displayed()
        except Exception as e:
            print(f"car_model_is_visible failed: {e}")
            return False