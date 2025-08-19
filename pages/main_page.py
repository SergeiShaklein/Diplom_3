import allure

import locators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BaseAction

class MainPageAction(BaseAction):
    with allure.step ('Кликаем по кнопке "Личный кабинет"'):
        def click_private_area(self):
            locator = locators.main_page_locators.MainPageLocators
            self.click_element(locator.button_private_area)

    with allure.step ('Кликаем по кнопке "Конструктор"'):
        def click_constructor(self):
            locator = locators.main_page_locators.MainPageLocators
            self.wait_clickable_and_click(locator.button_construction)

    with allure.step ('Кликаем по кнопке "Лента заказов"'):
        def click_order_feed(self):
            locator = locators.main_page_locators.MainPageLocators
            self.click_element(locator.button_order_feed)

    with allure.step ('Кликаем по кнопке "Оформить заказ"'):
        def click_button_place_order(self):
            locator = locators.main_page_locators.MainPageLocators
            self.wait_clickable_and_click(locator.place_order)

    with allure.step ('Кликаем на ингредиент "Краторная булка N-200i"'):
        def click_crater_bun(self):
            locator = locators.main_page_locators.MainPageLocators
            self.wait_clickable_and_click(locator.ingredient_crater_bun)

    with allure.step ('Кликаем на крестик в окне "Детали ингредиента"'):
        def click_close_button(self):
            locator = locators.main_page_locators.MainPageLocators
            self.click_element(locator.close_details_ingredient_button)

    with allure.step ('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
        def move_bun_to_basket(self):
            locator = locators.main_page_locators.MainPageLocators
            ingredient = self.find_element_with_wait(locator.ingredient_crater_bun)
            basket = self.find_element_with_wait(locator.basket_area)
            self.drag_and_drop_element(source=ingredient, target=basket)

    with allure.step ('Кликаем по кнопке "Войти в аккаунт"'):
        def click_button_entrance_account(self):
            locator = locators.main_page_locators.MainPageLocators
            self.click_element(locator.button_entrance_account)

    with allure.step ('Получаем текст заголовка Конструктора'):
        def get_constructor_header(self):
            locator = locators.main_page_locators.MainPageLocators
            return self.get_text_element(locator.header_create_burger)

    with allure.step ('Получаем текст заголовка окна "Детали ингредиента"'):
        def get_detail_ing_header(self):
            locator = locators.main_page_locators.MainPageLocators
            return self.get_text_element(locator.header_details_ingredient)

    with allure.step ('Получаем название ингредиента "Краторная булка N-200i"'):
        def get_name_crater_bun(self):
            locator = locators.main_page_locators.MainPageLocators
            return self.get_text_element(locator.name_crater_bun)

    with allure.step ('Получаем значение счетчика иингредиента "Краторная булка N-200i"'):
        def get_value_counter(self):
            locator = locators.main_page_locators.MainPageLocators
            self.wait_for_element(locator.ingredient_counter)
            count_bun = self.get_text_element(locator.ingredient_counter)
            return int(count_bun)

    with allure.step ('Ожидаем появления крестика в окне "Детали ингредиента"'):
        def wait_close_button(self):
            locator = locators.main_page_locators.MainPageLocators
            self.wait_for_element(locator.close_details_ingredient_button)

    with allure.step ('Ожидаем видимости окна "Детали ингредиента"'):
        def detail_ing_is_visible(self):
            locator = locators.main_page_locators.MainPageLocators
            self.is_element_visible(locator.close_details_ingredient_button)
