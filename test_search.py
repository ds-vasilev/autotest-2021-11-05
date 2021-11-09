import pytest
from pages.search import GoogleSearchPage
from pages.result import GoogleResultPage
from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    """Фикстура на загрузку Хрома, неявные ожидания 10 сек, ожидания действий и закрытие браузера"""
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()



@pytest.mark.parametrize(
    #параметризизация позитивного и негативного по параметрам из задания
    "LOOKING_FOR,EXPECTED",
    [("1 * 2 - 3 + 1 =", 0), pytest.param("1 * 2 - 3 + 1 =", 5000, marks=pytest.mark.xfail)],
)


def test_search_and_calculate(browser, LOOKING_FOR, EXPECTED):
    """Тест на открытие поиска Гугла, подачу в него слова "Калькулятор",
    расчет в калькуляторе данных из параметризации и две проверки
    """
    PHRASE = 'калькулятор'

    search_page = GoogleSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    result_page = GoogleResultPage(browser)
    result_page.calculate(LOOKING_FOR)
    assert EXPECTED == int(result_page.result_check_value())

    #калькулятоп гугла возвращает данные в форме "1 × 3 + 2 - 1 ÷ 1 =" с измененными символами
    assert LOOKING_FOR == result_page.memory_check_count().replace('×','*')
