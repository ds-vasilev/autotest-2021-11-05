import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# запрос на подачу языка (1)
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")


    # передаем в user_language язык, переданный в командную строку из (1)
    user_language = request.config.getoption("language")

    options = Options()
    
    # запуск браузера с указанным user_language
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()






