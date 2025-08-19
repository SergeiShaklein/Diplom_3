import allure

import data
from pages.main_page import MainPageAction
from pages.order_page import OrderPageAction


@allure.feature('Основная функциональность')
@allure.story ('Проверка основной функциональности веб-приложения Stellar Burgers')

class TestCheckMainPage:

    @allure.title ('Проверка перехода по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        main_page = MainPageAction(driver)

        with allure.step('Кликаем на кнопку "Личный кабинет"'):
            main_page.click_private_area()

        with allure.step('Кликаем на кнопку "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Определяем текст заголовка у открывшейся страницы'):
            header_text = main_page.get_constructor_header()

        with allure.step('Проверяем, что видим заголовок "Соберите бургер"'):
            assert header_text == data.Headers.header_create_burger


    @allure.title ('Проверка перехода по клику на раздел «Лента заказов»')
    def test_click_to_order_feed(self, driver):
        main_page = MainPageAction(driver)
        order_page = OrderPageAction(driver)

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Ожидаем загрузки страницы "Лента заказов"'):
            order_page.wait_header_order_feed()

        with allure.step('Определяем текст заголовка у открывшейся страницы'):
            header_text = order_page.get_order_feed_header()

        with allure.step('Проверяем, что видим заголовок "Лента заказов"'):
            assert header_text == data.Headers.header_order_feed


    @allure.title ('Проверка появления всплывающего окна с деталями ингредиента по клику на ингредиент')
    def test_click_to_ingredient(self, driver):
        main_page = MainPageAction(driver)

        with allure.step('Кликаем на ингредиент "Краторная булка N-200i"'):
            main_page.click_crater_bun()

        with allure.step('Определяем, что открылось окно с заголовком'):
            header_text = main_page.get_detail_ing_header()

        with allure.step('Определяем, что в окне есть название ингредиента'):
            bun_name = main_page.get_name_crater_bun()

        with allure.step('Проверяем, что заголовок - "Детали ингредиента", а название - "Краторная булка N-200i"'):
            assert header_text == data.Headers.header_detail_ingredient and bun_name == data.Headers.crater_bun_name


    @allure.title ('Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик')
    def test_click_to_close_button(self, driver):
        main_page = MainPageAction(driver)

        with allure.step('Кликаем на ингредиент "Краторная булка N-200i"'):
            main_page.click_crater_bun()

        with allure.step('Определяем появление крестка в окне "Детали ингредиента"'):
            main_page.wait_close_button()

        with allure.step('Кликаем на крестик в окне "Детали ингредиента"'):
            main_page.click_close_button()

        with allure.step('Проверяем, что окно "Детали ингредиента" закрылось'):
            assert not main_page.detail_ing_is_visible()


    @allure.title ('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter(self, driver):
        main_page = MainPageAction(driver)

        with allure.step('Определяем изначальное значение счетчика ингредиент "Краторная булка N-200i"'):
            start_count = main_page.get_value_counter()

        with allure.step ('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            main_page.move_bun_to_basket()

        with allure.step('Определяем новое значение счетчика ингредиент "Краторная булка N-200i"'):
            finish_count = main_page.get_value_counter()
            assert finish_count == start_count + 2
