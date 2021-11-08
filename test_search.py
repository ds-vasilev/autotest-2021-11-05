import pytest
from pages.search import GoogleSearchPage
from pages.result import GoogleResultPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_and_calculate(browser):
    PHRASE = 'калькулятор'
    LOOKING_FOR = "1 * 2 - 3 + 1 ="

    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = GoogleResultPage(browser)
    result_page.calculate(LOOKING_FOR)
    assert eval(LOOKING_FOR[:-1]) == int(result_page.result_check_value())

    #гугл возвращает данные в такой форме  (1 × 3 + 2 - 1 ÷ 1 =)
    assert LOOKING_FOR == result_page.memory_check_count().replace('×','*')
