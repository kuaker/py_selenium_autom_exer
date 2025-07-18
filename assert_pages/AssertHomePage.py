from locators.nav_bar_locators import NavBarLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage

class AssertHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_elements_present(self):
        assert (self.find_element(NavBarLocators.nav_bar).is_displayed()) == True
        assert (self.find_element(HomePageLocators.h1).is_displayed()) == True
        assert (self.find_element(HomePageLocators.h2).is_displayed()) == True