import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Select: desired locale')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Select: chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser_name unrecognized or language is incorrect')
    yield browser
    browser.quit()
