from .base_page import BasePage
from .locators import ResultLocators

class GoogleResultPage(BasePage):

    def calculate(self, looking_for):
        calculate_input = self.browser.find_element(*ResultLocators.CALC_FIELD)
        calculate_input.send_keys(looking_for)

    def result_check_value(self):
        result_check = self.browser.find_element(*ResultLocators.RESULT_FIELD).text
        return (result_check)

    def memory_check_count(self):
        memory_check = self.browser.find_element(*ResultLocators.MEMORY_FIELD).text
        return (memory_check)