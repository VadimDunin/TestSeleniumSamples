class MainPage:
    def __init__(self, app):
        self.app = app

    def open_page(self):
        self.app.get("http://www.penzgtu.ru")