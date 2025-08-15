import locators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BaseAction


class OrderPageAction(BaseAction):
    # Получения значения "Выполнено за все время"
    def get_value_all_time(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        value_all_time = self.get_text_element(locator.counter_all_time)
        return f'0{value_all_time}'

    # Получения значения счетчика "Выполнено за сегодня"
    def get_value_today(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        value_today = self.get_text_element(locator.counter_today)
        return value_today

    # Получение номера сделанного заказа
    def get_our_order_number(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_disappear_animation()
        our_order_number = self.get_text_element(locator.our_order_number)
        return f'0{our_order_number}'

    # Получение номера заказа в блоке "В работе"
    def get_number_in_working(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_disappear_message()
        number_in_working = self.get_text_element(locator.number_in_working)
        return number_in_working

    # Ожидание заголовка "Лента заказов"
    def wait_header_order_feed(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_for_element(locator.header_order_feed)

    # Ожидание загрузки счетчика Выполнено за сегодня
    def wait_counter_today(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_for_element(locator.counter_today)

    # Ожидание исчезновения анимации
    def wait_disappear_animation(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_loading_to_disappear(locator.disappear_animation)

    # Ожидание активности модального окна "идентификатор заказа"
    def close_button_is_clickable(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_clickable(locator.close_button_modal_window)

    # Ожидание исчезновения сообщения Все текущие заказы готовы!
    def wait_disappear_message(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.wait_loading_to_disappear(locator.disappear_message)

    # Клик на крестик в окне идентификатор заказа
    def click_close_modal_window(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        self.click_element(locator.close_button_modal_window)

    # Получение текста заголовка Лента заказов
    def get_order_feed_header(self):
        locator = locators.order_feed_page_locators.OrderFeedPageLocators
        return self.get_text_element(locator.header_order_feed)
