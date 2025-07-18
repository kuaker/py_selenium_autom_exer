from conftest import driver
from pages.base_page import BasePage
from locators.nav_bar_locators import NavBarLocators

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_products(self):
        print('HOLA')
        self.find_element(NavBarLocators.nav_bar)