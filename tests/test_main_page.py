import allure
import helpers

@allure.feature('Основная функциональность')
@allure.story ('Проверка основной функциональности веб-приложения Stellar Burgers')

class TestCheckMainPage:

    @allure.title ('Проверка перехода по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        click_locator = helpers.ClickByLocator(driver)
        get_text = helpers.TextLocator(driver)

        with allure.step('Кликаем на кнопку Личный кабинет"'):
            click_locator.click_private_area()

        with allure.step('Кликаем на кнопку "Конструктор"'):
            click_locator.click_constructor()  # кликаем Конструктор

        with allure.step('Определяем текст заголовка у открывшейся страницы'):
            header_text = get_text.get_constructor_header()

        with allure.step('Проверяем, что видим заголовок "Соберите бургер"'):
            assert header_text == 'Соберите бургер'


    @allure.title ('Проверка перехода по клику на раздел «Лента заказов»')
    def test_click_to_order_feed(self, driver):
        click_locator = helpers.ClickByLocator(driver)
        wait_locator = helpers.WaitLocator(driver)
        get_text = helpers.TextLocator(driver)

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            click_locator.click_order_feed()

        with allure.step('Ожидаем загрузки страницы "Лента заказов"'):
            wait_locator.wait_header_order_feed()

        with allure.step('Определяем текст заголовка у открывшейся страницы'):
            header_text = get_text.get_order_feed_header()

        with allure.step('Проверяем, что видим заголовок "Лента заказов"'):
            assert header_text == 'Лента заказов'


    @allure.title ('Проверка появления всплывающего окна с деталями ингредиента по клику на ингредиент')
    def test_click_to_ingredient(self, driver):
        click_locator = helpers.ClickByLocator(driver)
        get_text = helpers.TextLocator(driver)

        with allure.step('Кликаем на ингредиент "Краторная булка N-200i"'):
            click_locator.click_crater_bun()

        with allure.step('Определяем, что открылось окно с заголовком'):
            header_text = get_text.get_detail_ing_header()

        with allure.step('Определяем, что в окне есть название ингредиента'):
            bun_name = get_text.get_name_crater_bun()

        with allure.step('Проверяем, что заголовок - "Детали ингредиента", а название - "Краторная булка N-200i"'):
            assert header_text == "Детали ингредиента" and bun_name == "Краторная булка N-200i"



    @allure.title ('Проверка закрытия всплывающего окна с деталями ингредиента по клику на крестик')
    def test_click_to_close_button(self, driver):
        click_locator = helpers.ClickByLocator(driver)
        wait_locator = helpers.WaitLocator(driver)

        with allure.step('Кликаем на ингредиент "Краторная булка N-200i"'):
            click_locator.click_crater_bun()

        with allure.step('Определяем появление крестка в окне "Детали ингредиента"'):
            wait_locator.wait_close_button()

        with allure.step('Кликаем на крестик в окне "Детали ингредиента"'):
            click_locator.click_close_button()

        with allure.step('Проверяем, что окно "Детали ингредиента" закрылось'):
            assert not wait_locator.detail_ing_is_visible()


    @allure.title ('Проверка, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter(self, driver):
        get_text = helpers.TextLocator(driver)
        click_locator = helpers.ClickByLocator(driver)

        with allure.step('Определяем изначальное значение счетчика ингредиент "Краторная булка N-200i"'):
            start_count = get_text.get_value_counter()

        with allure.step ('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            click_locator.move_bun_to_basket()

        with allure.step('Определяем новое значение счетчика ингредиент "Краторная булка N-200i"'):
            finish_count = get_text.get_value_counter()
            assert finish_count == start_count + 2
