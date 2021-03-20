from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Select: desired locale')
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Select: chrome or firefox')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument('--headless')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(f'--browser_name {browser_name} not supported')
    yield browser
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # browser.save_screenshot(f'screentshot-{now}.png')
    browser.quit()


@pytest.fixture(scope='function')
def user_language(request):
    user_language = request.config.getoption('language')
    yield user_language
