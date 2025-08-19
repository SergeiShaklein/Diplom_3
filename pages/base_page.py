import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    with allure.step ('Click'):
        def click_element(self, locator):
            self.driver.find_element(*locator).click()

    with allure.step ('Get text'):
        def get_text_element(self, locator, timeout=10):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text

    with allure.step ('Wait change text'):
        def wait_for_text_change(self, locator, timeout=10):
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            initial_text = element.text
            WebDriverWait(self.driver, timeout).until(lambda d: element.text != initial_text)
            return element.text

    with allure.step ('Wait visibility element'):
        def wait_for_element(self, locator, timeout=70):
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    with allure.step ('Wait element is displayed'):
        def is_element_visible(self, locator):
            elements = self.driver.find_elements(*locator)
            return len(elements) > 0 and elements[0].is_displayed()

    with allure.step ('Drag and drop'):
        def drag_and_drop_element(self, source, target):
            drag_and_drop(self.driver, source, target)

    with allure.step ('Find element'):
        def find_element_with_wait(self, locator):
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)

    with allure.step ('Fill field'):
        def fill_field(self, locator, data_reg):
            self.driver.find_element(*locator).send_keys(data_reg)

    with allure.step ('Wait clickable and click'):
        def wait_clickable_and_click(self, locator):
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()

    with allure.step ('Wait clickable'):
        def wait_clickable(self, locator):
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))

    with allure.step ('Wait invisibility'):
        def wait_loading_to_disappear(self, locator):
            WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located(locator))
