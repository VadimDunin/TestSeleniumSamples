from links import links


class MainPage:

    def __init__(self, browser):
        self.browser = browser

    def open_page(self):
        self.browser.get(links.main_page)