import pytest
from selenium import webdriver
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import *

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(main_site)
    driver.refresh()
    yield driver
    driver.quit()

@pytest.fixture
def authorization(driver):

    driver.find_element(*Locators.button_entrance_account).click() # ищем кнопку Войти в аккаунт и кликаем
    driver.find_element(*Locators.field_email).send_keys(Credantial.email) # заполняем поле email
    driver.find_element(*Locators.field_password).send_keys(Credantial.password) # заполняем поле Пароль
    driver.find_element(*Locators.button_entrance_in_login_page).click() # кликаем на Войти
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.place_order)) # ждем загрузки кнопки Оформить заказ (доступна только после авторизации)

    return driver

#
# import pytest  # Обязательно импортируем pytest
# from selenium import webdriver
#
# class WebdriverFactory:
#     @staticmethod
#     def get_webdriver(browser_name):
#         if browser_name == "firefox":
#             return webdriver.Firefox()
#         elif browser_name == "chrome":
#             return webdriver.Chrome()
#         else:
#             raise ValueError(f"Unsupported browser: {browser_name}")
#
# # Эта функция добавляет возможность передачи параметра --browser в командной строке pytest
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser", action="store", default="chrome", help="Выбор браузера: 'chrome' или 'firefox'."
#     )
#
# @pytest.fixture
# def driver(request):
#     # Получаем параметр браузера из командной строки
#     browser_name = request.config.getoption("--browser")
#     # Создаем и возвращаем соответствующий драйвер
#     driver = WebdriverFactory.get_webdriver(browser_name)
#     driver.maximize_window()  # Открытие окна на весь экран
#     yield driver
#     driver.quit()
