from links import links
from main_page.main_page_locators import main_page_locators
from main_page.main_page_test_data import test_data_cities


def test_open_main_page(browser):
    browser.get(links.main_page)
    browser.get(links.page_request)
    browser.get(links.page_corrupt)
    browser.get(links.page_gosuslugi)
    browser.get(links.main_page)


def test_check_cities_list(browser):
    cities = browser.find_elements_by_css_selector(main_page_locators.cities)
    for found_city in cities:
        assert found_city.text in test_data_cities

def test_request_answerts(browser):
    browser.get(links.page_request)
    answers_buttons = browser.find_elements_by_css_selector(main_page_locators.answers_buttons)
    labels = browser.find_elements_by_css_selector(main_page_locators.labels_o)