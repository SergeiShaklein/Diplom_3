import time

from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # Действие клик на любом явном локаторе
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    # Получение текста из локатора
    def get_text_element(self, locator):
        time.sleep(2)
        return self.driver.find_element(*locator).text

    # Ожидание элемента локатора
    def wait_for_element(self, locator, timeout=70):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Проверка, виден ли локатор на странице
    def is_element_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0 and elements[0].is_displayed()

    # Перетащить элемент локатора
    def drag_and_drop_element(self, source, target):
        drag_and_drop(self.driver, source, target)

    # Поиск элемента по локатору
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    # Заполнить поле
    def fill_field(self, locator, data_reg):
        self.driver.find_element(*locator).send_keys(data_reg)

    # Ждем пока элемент станет кликабельным и кликаем
    def wait_clickable_and_click(self, locator):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # Ждем пока элемент станет кликабельным
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))

    # Ждем исчезновения элемента
    def wait_loading_to_disappear(self, locator):
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located(locator))
