from selenium.webdriver.common.by import By

class HomePageLocators:
    carousel_inner = (By.CLASS_NAME, '.carousel-inner')
    corousel_left_arrow = (By.CLASS_NAME,'.left.control-carousel hidden-xs')
    corousel_right_arrow = (By.CLASS_NAME, '.right.control-carousel hidden-xs')

    h1 = (By.TAG_NAME, 'h1')
    h2 = (By.TAG_NAME, 'h2')