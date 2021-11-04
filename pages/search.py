from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .locators import SearchLocators

class GoogleSearchPage:
    URL = 'https://www.google.com'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*SearchLocators.SEARCH_FIELD)
        search_input.send_keys(phrase + Keys.RETURN)