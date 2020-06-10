from selenium.webdriver.chrome.webdriver import WebDriver
import pytest, time


wd = WebDriver(executable_path="C:\Temp\ChromeDriver\83.exe")
wd.implicitly_wait(5)
url = ""


class User:
    def __init__(self, displayed_username=None, password=None, mail=None):
        self.displayed_username = displayed_username
        self.password = password
        self.mail = mail


Vadim = User('Вадим', 'Xxbzzczxxax2020', 'duninv@gmail.com')
timeout = 3


def test_open_home_page():
    wd.get("https://emex.ru")
    wd.maximize_window()
    button_login = wd.find_element_by_css_selector('button.Link__LinkItem-hikcvf-0.kBGzmi.TopHeader__LoginButton-sc-13d6ldt-4.grbxWr')
    button_login.click()
    login_field = wd.find_element_by_name('login')
    password_field = wd.find_element_by_name('password')
    login_field.send_keys(Vadim.mail)
    password_field.send_keys(Vadim.password)
    button_enter = wd.find_element_by_css_selector('button.Button__ButtonItem-sc-1lg7vvv-2.hBBlZe.SignIn__LogInButton-sc-14u62jc-9.bjXHrz')
    button_enter.click()
    time.sleep(timeout)
    login_name = wd.find_element_by_css_selector("span.UserControls__UserName-sc-1lqz9cn-4.bcScNr").text
    assert str(login_name).strip(" ") == Vadim.displayed_username
    user_menu = wd.find_element_by_css_selector('div.Button__Content-sc-1lg7vvv-0.erUssK > span')
    user_menu.click()
    button_users_menu_quit = wd.find_element_by_css_selector('button.Button__ButtonItem-sc-1lg7vvv-2.lgbJSW.UserMenu__ExitButton-sc-12qog7b-0.cuaza-d')
    button_users_menu_quit.click()
    time.sleep(timeout)
    wd.quit()