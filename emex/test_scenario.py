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
User1 = User('Ivan', '1qaz@WSX', 'sharpshooter47@yanadex.ru')
timeout = 3


class HomePageLocators:
    login_button = 'button.Link__LinkItem-hikcvf-0.kBGzmi.TopHeader__LoginButton-sc-13d6ldt-4.grbxWr'
    login_field = 'login'
    password_field = 'password'
    enter_button = 'button.Button__ButtonItem-sc-1lg7vvv-2.hBBlZe.SignIn__LogInButton-sc-14u62jc-9.bjXHrz'
    login_name_text = "span.UserControls__UserName-sc-1lqz9cn-4.bcScNr"
    users_menu = 'div.Button__Content-sc-1lg7vvv-0.erUssK > span'
    users_menu_quit_buttton = 'button.Button__ButtonItem-sc-1lg7vvv-2.lgbJSW.UserMenu__ExitButton-sc-12qog7b-0.cuaza-d'


def test_open_home_page():
    wd.get("https://emex.ru")
    wd.maximize_window()
    button_login = wd.find_element_by_css_selector(HomePageLocators.login_button)
    button_login.click()
    login_field = wd.find_element_by_name(HomePageLocators.login_field)
    password_field = wd.find_element_by_name(HomePageLocators.password_field)
    login_field.send_keys(Vadim.mail)
    password_field.send_keys(Vadim.password)
    button_enter = wd.find_element_by_css_selector(HomePageLocators.enter_button)
    button_enter.click()
    time.sleep(timeout)
    login_name = wd.find_element_by_css_selector(HomePageLocators.login_name_text).text
    assert str(login_name).strip(" ") == Vadim.displayed_username
    user_menu = wd.find_element_by_css_selector(HomePageLocators.users_menu)
    user_menu.click()
    button_users_menu_quit = wd.find_element_by_css_selector(HomePageLocators.users_menu_quit_buttton)
    button_users_menu_quit.click()
    time.sleep(timeout)
    wd.quit()