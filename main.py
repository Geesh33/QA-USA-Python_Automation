
from selenium import webdriver
from selenium.webdriver.common.by import By

import data
from helpers import is_url_reachable
from data import URBAN_ROUTES_URL
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if is_url_reachable(URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
       self.driver.get(URBAN_ROUTES_URL)
       routes_page = UrbanRoutesPage(self.driver)
       routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
       routes_page.select_supportive_plan()
       assert routes_page.get_current_selected_plan() == 'Supportive'

    def test_fill_phone_number(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_phone_number(data.PHONE_NUMBER)
        phone_value = self.driver.find_element(By.ID, 'phone').get_attribute('value')
        assert phone_value == data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_card_details(data.CARD_NUMBER, data.EXPIRY_DATE, data.CVV)
        card_value = self.driver.find_element(By.ID, 'card-number').get_attribute('value')
        assert card_value.endswith("1111")

    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_driver_comment(data.DRIVER_COMMENT)
        comment_value = self.driver.find_element(By.ID, 'driver-comment').get_attribute('value')
        assert comment_value == data.DRIVER_COMMENT

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs()
        # Optionally assert some visible confirmation
        blanket_ordered = self.driver.find_element(By.ID, 'blanket-confirm').is_displayed()
        handkerchief_ordered = self.driver.find_element(By.ID, 'handkerchief-confirm').is_displayed()
        assert blanket_ordered and handkerchief_ordered

    def test_order_2_ice_creams(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_multiple_ice_creams(count=2)
        # Assert visible confirmation exists
        confirmations = self.driver.find_elements(By.CLASS_NAME, 'ice-cream-confirmed')
        assert len(confirmations) >= 2

    def test_car_search_model_appears(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.car_model_is_visible()


    def test_order_2_ice_creams1(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_multiple_ice_creams(count=2)
        confirmations = self.driver.find_elements(By.CLASS_NAME, 'ice-cream-confirmed')
        assert len(confirmations) >= 2


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()