from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import SearchLocators

class GoogleSearchPage(BasePage):
    URL = 'https://www.google.com'

    def search(self, phrase):
        search_input = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        search_input.send_keys(phrase + Keys.RETURN)