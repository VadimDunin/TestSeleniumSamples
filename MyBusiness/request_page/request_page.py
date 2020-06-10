from links import links
from request_page import locators, request_test_data


class RequestPage:

    def __init__(self, app):
        self.browser = app

    def open_page(self):
        self.browser.get(links.page_request)

    def check_answer_labels(self):
        res = True
        found_labels = self.browser.find_elements_by_css_selector(locators.locators.label_option)
        if len(request_test_data.answers) != len(found_labels):
            res = False
        for label in found_labels:
            if label not in request_test_data.answers:
                res = False
                break
        return res