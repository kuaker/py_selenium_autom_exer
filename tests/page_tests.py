from assert_pages.AssertHomePage import AssertHomePage
from common import Config
from pages.home_page import HomePage

def test_check_objects(driver):
    homepage = HomePage(driver)
    homepage.load(Config.BASE_URL)
    asserthomepage = AssertHomePage(driver)
    asserthomepage.is_elements_present()

def test_go_to_product(driver):
    homepage = HomePage(driver)
    homepage.load(Config.BASE_URL)
    homepage.click_on_products()

