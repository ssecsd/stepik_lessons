import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Select: chrome or firefox')

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError('--browser_name unrecognized')
    yield browser
    browser.quit()