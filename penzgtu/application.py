from selenium.webdriver.chrome.webdriver import WebDriver
from main_page import MainPage


class Application:
    def __init__(self):
        self.app = WebDriver(executable_path="C:\Temp\ChromeDriver\83.exe")
        self.app.implicitly_wait(5)
        self.main_page = MainPage(self)

    def quit(self):
        self.app.quit()

    def open_page(self):
        self.app.get("http://www.penzgtu.ru")