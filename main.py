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
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        assert routes_page.get_from() == data.ADDRESS_FROM
        assert routes_page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive()
        assert routes_page.get_active_plan() == "Supportive"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.select_phone()
        routes_page.enter_phone(data.PHONE_NUMBER)
        routes_page.next_button()
        routes_page.code_field()
        routes_page.confirm_button()
        assert routes_page.get_phone() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive()
        routes_page.select_payment_method()
        routes_page.click_add_card()
        routes_page.enter_card_number(data.CARD_NUMBER)
        routes_page.enter_card_code(data.CARD_CODE)
        routes_page.click_on_title()
        routes_page.click_link_button()
        assert routes_page.get_current_payment_method_type() == 'Card'



    def test_comment_for_driver(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.enter_message(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_current_message() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive()
        routes_page.blanket_and_hanker()
        assert routes_page.get_slider_selected() == 'true'


    def test_order_2_ice_creams(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive()
        routes_page.select_ice_cream()
        routes_page.select_ice_cream()
        assert routes_page.get_ice_cream() == '2'



    def test_car_search_model_appears(self):
        self.driver.get(URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_from(data.ADDRESS_FROM)
        routes_page.enter_to(data.ADDRESS_TO)
        routes_page.click_call_a_taxi()
        routes_page.click_supportive()
        routes_page.enter_message(data.MESSAGE_FOR_DRIVER)
        routes_page.select_order_button()
        assert routes_page.get_car_search_title() == 'Car search'




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()