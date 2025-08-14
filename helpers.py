import data
import locators
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# -- Базовые действия --
###########################################################################
class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # Действие клик на любом явном локаторе
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    # Получение текста из локатора
    def get_text_element(self, locator):
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
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except Exception as e:
            print(f"Не удалось найти элемент: {locator}. Ошибка: {e}")
            return None

    # Заполнить поле
    def fill_field(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    # Ждем пока элемент станет кликабельным и кликаем
    def wait_clickable_and_click(self, locator):
        element = WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    # Ждем пока элемент станет кликабельным
    def wait_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))

    # Ждем исчезновения элемента
    def wait_loading_to_disappear(self, locator):
        WebDriverWait(self.driver, 25).until(EC.invisibility_of_element_located(locator))

    # Ожидание изменений
    def wait_changes(self, changes, timeout=10):
        WebDriverWait(self.driver, timeout).until(changes)


# -- Клики по элементам--
###########################################################################
class ClickByLocator(BaseAction):
    # Клик на кнопке Личный кабинет
    def click_private_area(self):
        self.click_element(locators.Locators.button_private_area)

    # Клик на кнопке Конструктор
    def click_constructor(self):
        self.click_element(locators.Locators.button_construction)

    # Клик на кнопке Лента заказов
    def click_order_feed(self):
        self.click_element(locators.Locators.button_order_feed)

    # Клик на ингредиент "Краторная булка N-200i"
    def click_crater_bun(self):
        self.click_element(locators.Locators.ingredient_crater_bun)

    # Клик на крестик в окне "Детали ингредиента"
    def click_close_button(self):
        self.click_element(locators.Locators.close_details_ingredient_button)

    # Перетаскивание ингредиента "Краторная булка N-200i" в корзину
    def move_bun_to_basket(self):
        ingredient = self.find_element_with_wait(locators.Locators.ingredient_crater_bun)
        basket = self.find_element_with_wait(locators.Locators.basket_area)
        self.drag_and_drop_element(source=ingredient, target=basket)

    # Клик на кнопку "Войти в аккаунт"
    def click_button_entrance_account(self):
        self.click_element(locators.Locators.button_entrance_account)

    # Клик на кнопку "Войти"
    def click_button_entrance_in_login_page(self):
        self.click_element(locators.Locators.button_entrance_in_login_page)

    # Клик на кнопку "Оформить заказ"
    def click_button_place_order(self):
        overlay = self.find_element_with_wait(locators.Locators.disappear_modal_window)
        if overlay:  # Проверяем, был ли найден элемент
            self.driver.execute_script("arguments[0].style.display = 'none';", overlay)
        self.wait_clickable_and_click(locators.Locators.place_order)

    # Клик на крестик в окне идентификатор заказа
    def click_close_modal_window(self):
        self.click_element(locators.Locators.close_button_modal_window)

# -- Получение текста из элементов--
###########################################################################
class TextLocator(BaseAction):
    # Получения текста заголовка Конструктора
    def get_constructor_header(self):
        return self.get_text_element(locators.Locators.header_create_burger)

    # Получения текста заголовка Лента заказов
    def get_order_feed_header(self):
        return self.get_text_element(locators.Locators.header_order_feed)

    # Получения текста заголовка окна "Детали ингредиента"
    def get_detail_ing_header(self):
        return self.get_text_element(locators.Locators.header_details_ingredient)

    # Получения названия ингредиента "Краторная булка N-200i"
    def get_name_crater_bun(self):
        return self.get_text_element(locators.Locators.name_crater_bun)

    # Получения значения счетчика ингредиентов
    def get_value_counter(self):
        count_bun = self.get_text_element(locators.Locators.ingredient_counter)
        return int(count_bun)

    # Получения значения "Выполнено за все время"
    def get_value_all_time(self):
        value_all_time = self.get_text_element(locators.Locators.counter_all_time)
        return value_all_time

    # Получения значения счетчика "Выполнено за сегодня"
    def get_value_today(self):
        value_today = self.get_text_element(locators.Locators.counter_today)
        return value_today

    # Получение номера сделанного заказа
    def get_our_order_number(self):
        our_order_number = self.get_text_element(locators.Locators.our_order_number)
        return f'0{our_order_number}'

    # Получение номера заказа в блоке "В работе"
    def get_number_in_working(self):
        number_in_working = self.get_text_element(locators.Locators.number_in_working)
        return number_in_working

    # Получение последнего номера заказа в блоке "Готовы"
    def get_number_in_ready(self):
        self.get_text_element(locators.Locators.number_in_ready)

    # Заполнение поля email
    def fill_email(self):
        self.fill_field(locators.Locators.field_email, data.Credantial.email)

    # Заполнение поля password
    def fill_password(self):
        self.fill_field(locators.Locators.field_password, data.Credantial.password)


# -- Ожидание элементов--
###########################################################################
class WaitLocator(BaseAction):
    def __init__(self, driver):
        super().__init__(driver)
        self.text_locator = TextLocator(driver)

    # Ожидание заголовка "Лента заказов"
    def wait_header_order_feed(self):
        self.wait_for_element(locators.Locators.header_order_feed)

    # Ожидание крестика в окне "Детали ингредиента"
    def wait_close_button(self):
        self.wait_for_element(locators.Locators.close_details_ingredient_button)

    # Ожидание появления нашего идентификатором заказа в блоке "В работе"
    def wait_identifier_in_work(self):
        self.wait_for_element(locators.Locators.number_in_working)

    # Ожидание появления нашего идентификатором заказа в блоке Готовы
    def wait_identifier_in_ready(self):
        self.wait_for_element(locators.Locators.number_in_ready)

    # Ожидание исчезновения анимации
    def wait_disappear_animation(self):
        self.wait_loading_to_disappear(locators.Locators.disappear_animation)

    # Ожидание исчезновения модального окна
    def wait_disappear_modal_window(self):
        self.wait_loading_to_disappear(locators.Locators.disappear_modal_window)

    # Ожидание видимости окна "Детали ингредиента"
    def detail_ing_is_visible(self):
        self.is_element_visible(locators.Locators.close_details_ingredient_button)

    # Ожидание активности модального окна "идентификатор заказа"
    def close_button_is_clickable(self):
        self.wait_clickable(locators.Locators.close_button_modal_window)

    # Ожидание исчезновения сообщения Все текущие заказы готовы!
    def wait_disappear_message(self):
        self.wait_loading_to_disappear(locators.Locators.disappear_message)

