import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import helpers
from helpers import retrieve_phone_code


class UrbanRoutesPage:
    FROM_FIELD = (By.XPATH,"//input[@id='from']")
    TO_FIELD = (By.XPATH,"//input[@id='to']")
    CALL_A_TAXI = (By.XPATH,"//button[text()='Call a taxi']")
    SUPPORTIVE = (By.XPATH,"//div[@class='tcard-title' and text()='Supportive']")
    SELECT_PHONE = (By.XPATH,"//div[@class='np-button']")
    PHONE_FIELD = (By.XPATH,"//input[@id='phone']")
    NEXT_BUTTON = (By.XPATH,"//button[@type='submit' and @class='button full' and text()='Next']")
    CODE_FIELD = (By.XPATH,"//input[@class='input' and @placeholder='xxxx']")
    TCARD_ACTIVE = (By.XPATH,"//div[@class='tcard active']//div[@class='tcard-title' and text()='Supportive']")
    CONFIRM_BUTTON = (By.XPATH,"//button[@type='submit' and @class='button full' and text()='Confirm']")
    PHONE_ENTER_FIELD = (By.XPATH,"//div[@class='np-text']")
    PAYMENT_METHOD = (By.XPATH,"//div[@class='pp-text' and text()='Payment method']")
    ADD_CARD = (By.XPATH,"//div[@class='pp-title' and text()='Add card']")
    CARD_NUMBER = (By.XPATH,"//input[@type='text' and @id='number' and @name='number' and @placeholder='1234 0000 4321' and @class='card-input']")
    CVV = (By.XPATH,"//input[@class='card-input' and @placeholder='12']")
    ADD_CARD_TITLE = (By.XPATH,"//div[@class='head' and text()='Adding a card']")
    LINK_BUTTON = (By.XPATH,"//button[@type='submit' and @class='button full' and text()='Link']")
    CARD_ADDED = (By.XPATH, "//div[@class='pp-title' and text()='Card']")
    PAYMENT_METHOD_TYPE = (By.XPATH,"//div[@class='pp-title' and text()='Card']")
    SELECT_COMMENT = (By.XPATH,"//div[@class='input-container']")
    ENTER_MESSAGE = (By.XPATH,"//input[@id='comment' and @placeholder='Get some whiskey']")
    BLANKET_AND_HANDKERCHIEF_BUTTON = (By.XPATH, "//span[contains(@class, 'slider') and contains(@class, 'round')]")
    INPUT_SLIDER = (By.XPATH, "//input[@type='checkbox' and @class='switch-input']")
    SELECT_ICE_CREAM_BUTTON = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    ICE_CREAM_COUNTER = (By.XPATH, "//div[@class='counter-value' and text()='2']")
    CLICK_ORDER_BUTTON = (By.XPATH, "//button[@type='button' and @class='smart-button']")
    CAR_SEARCH_TITLE = (By.XPATH, "//div[@class='order-header-title' and text()='Car search']")





    def __init__(self, driver):
        self.driver = driver

    def enter_from(self, address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)

    def enter_to(self, address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def click_call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI).click()

    def click_supportive(self):
        self.driver.find_element(*self.SUPPORTIVE).click()


    def get_active_plan(self):
        return self.driver.find_element(*self.TCARD_ACTIVE).text

    def select_phone(self):
        self.driver.find_element(*self.SELECT_PHONE).click()

    def enter_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def code_field(self):
        self.driver.find_element(*self.CODE_FIELD).send_keys(helpers.retrieve_phone_code(self.driver))

    def confirm_button(self):
        self.driver.find_element(*self.CONFIRM_BUTTON).click()

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_ENTER_FIELD).text

    def select_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)

    def enter_card_code(self, card_code):
        self.driver.find_element(*self.CVV).send_keys(card_code)

    def click_on_title(self):
        self.driver.find_element(*self.ADD_CARD_TITLE).click()

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()


    def get_current_payment_method_type(self):
        return self.driver.find_element(*self.CARD_ADDED).text

    def select_comment(self):
        self.driver.find_element(*self.SELECT_COMMENT).click()

    def enter_message(self, message_for_driver):
        self.driver.find_element(*self.ENTER_MESSAGE).send_keys(message_for_driver)

    def get_current_message(self):
        return self.driver.find_element(*self.ENTER_MESSAGE).get_attribute('value')

    def blanket_and_hanker(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEF_BUTTON).click()

    def get_slider_selected(self):
        return self.driver.find_element(*self.INPUT_SLIDER).get_attribute('checked')

    def select_ice_cream(self):
        self.driver.find_element(*self.SELECT_ICE_CREAM_BUTTON).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text

    def select_order_button(self):
        self.driver.find_element(*self.CLICK_ORDER_BUTTON).click()

    def get_car_search_title(self):
        return self.driver.find_element(*self.CAR_SEARCH_TITLE).text

