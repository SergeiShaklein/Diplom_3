import allure

import locators
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BaseAction


class OrderPageAction(BaseAction):
    with allure.step ('Получаем значение счетчика "Выполнено за все время"'):
        def get_value_all_time(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            value_all_time = self.get_text_element(locator.counter_all_time)
            return f'0{value_all_time}'

    with allure.step ('Получаем значения счетчика "Выполнено за сегодня"'):
        def get_value_today(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            value_today = self.get_text_element(locator.counter_today)
            return value_today

    with allure.step ('Получаем номер сделанного заказа'):
        def get_our_order_number(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_disappear_animation()
            our_order_number = self.get_text_element(locator.our_order_number)
            return f'0{our_order_number}'

    with allure.step ('Получаем номер заказа в блоке "В работе"'):
        def get_number_in_working(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_disappear_message()
            number_in_working = self.wait_for_text_change(locator.number_in_working)
            return number_in_working

    with allure.step ('Ожидаем появления заголовка "Лента заказов"'):
        def wait_header_order_feed(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_for_element(locator.header_order_feed)

    with allure.step ('Ожидаем загрузки счетчика "Выполнено за сегодня"'):
        def wait_counter_today(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_for_element(locator.counter_today)

    with allure.step ('Ожидание исчезновения анимации'):
        def wait_disappear_animation(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_loading_to_disappear(locator.disappear_animation)

    with allure.step ('Ожидаем активности кнопки закрытия окна "идентификатор заказа"'):
        def close_button_is_clickable(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_clickable(locator.close_button_modal_window)

    with allure.step ('Ожидаем исчезновения сообщения "Все текущие заказы готовы!"'):
        def wait_disappear_message(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.wait_loading_to_disappear(locator.disappear_message)

    with allure.step ('Кликаем на крестик в окне "идентификатор заказа"'):
        def click_close_modal_window(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            self.click_element(locator.close_button_modal_window)

    with allure.step ('Получаем текст заголовка "Лента заказов"'):
        def get_order_feed_header(self):
            locator = locators.order_feed_page_locators.OrderFeedPageLocators
            return self.get_text_element(locator.header_order_feed)
