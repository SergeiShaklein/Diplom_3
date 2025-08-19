import pytest
from data import *
from webdriver_factory import WebdriverFactory

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'.")

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebdriverFactory.get_webdriver(browser_name)
    driver.maximize_window()
    driver.get(main_site)
    driver.refresh()
    yield driver
    driver.quit()

# для запуска тестов в Firefox используем команду: pytest --browser=firefox
