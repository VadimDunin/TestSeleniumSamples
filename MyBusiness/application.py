from selenium.webdriver.chrome.webdriver import WebDriver
from settings import bin_path
from main_page.main_page import MainPage
from request_page.request_page import RequestPage


class Application:
    def __init__(self):
        self.driver = WebDriver(executable_path=bin_path)
        self.driver.implicitly_wait(5)
        self.main_page = MainPage(self)
        self.main_page = RequestPage(self)

    def get_elements_by_css(self, locator):
        return self.driver.find_elements_by_css_selector(locator)

    def close(self):
        self.driver.quit()