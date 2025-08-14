import allure
import helpers

@allure.feature('Функциональность раздела «Лента заказов»')
@allure.story ('Проверка функциональности счетчиков «Выполнено за всё время» и «Выполнено за сегодня», а также номера заказа в разделе «В работе»')

class TestCheckMainPage:

    # @allure.title ('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    # def test_counter_all_time(self, driver):
    #     wait_locator = helpers.WaitLocator(driver)
    #     visible_locator = helpers.VisibleLocator(driver)
    #     click_locator = helpers.ClickByLocator(driver)
    #     get_text = helpers.GetTextLocator(driver)
    #
    #     with allure.step ('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Нажимаем кнопку "Лента заказов"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Определяем текущий номер счетчика заказов «Выполнено за всё время»"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Нажимаем кнопку "Конструктор"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Нажимаем кнопку "Оформить заказ"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Ожидаем в окне "идентификатор заказа" номер нашего заказа'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Проверяем, что номер нашего заказа больше начального номера'):
    #         click_locator.move_bun_to_basket()
    #
    # @allure.title('Проверка, что при после оформления заказа его номер появляется в разделе «В работе»')
    # def test_order_in_process(self, driver):
    #     wait_locator = helpers.WaitLocator(driver)
    #     visible_locator = helpers.VisibleLocator(driver)
    #     click_locator = helpers.ClickByLocator(driver)
    #     get_text = helpers.GetTextLocator(driver)
    #
    #     with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step(
    #             'Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Нажимаем кнопку "Лента заказов"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Определяем текущий номер счетчика заказов «Выполнено за сегодня»"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Нажимаем кнопку "Конструктор"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Нажимаем кнопку "Оформить заказ"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Ожидаем в окне "идентификатор заказа" номер нашего заказа'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step ('Закрываем окно "идентификатор заказа"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Нажимаем кнопку "Лента заказов"'):
    #         click_locator.move_bun_to_basket()
    #
    #     with allure.step('Проверяем, что номер нашего в разделе "В работе"'):
    #         click_locator.move_bun_to_basket()

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_counter_all_time(self, driver):
        wait_locator = helpers.WaitLocator(driver)
        click_locator = helpers.ClickByLocator(driver)
        uses_text = helpers.TextLocator(driver)

        with allure.step('Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
            click_locator.click_button_entrance_account()
            uses_text.fill_email()
            uses_text.fill_password()
            click_locator.click_button_entrance_in_login_page()

        with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            click_locator.move_bun_to_basket()

        with allure.step('Нажимаем кнопку "Оформить заказ"'):
            wait_locator.wait_disappear_modal_window()
            click_locator.click_button_place_order()

        with allure.step('Ожидаем загрузки модульного окна с идентификатором заказа'):
            wait_locator.close_button_is_clickable()

        with allure.step('Определяем номер заказа в окне с идентификатором заказа'):
            wait_locator.wait_disappear_animation()
            our_order_number = uses_text.get_our_order_number()

        with allure.step('Закрываем модульное окна с идентификатором заказа'):
            click_locator.click_close_modal_window()

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            click_locator.click_order_feed()

        with allure.step('Ожидаем загрузки страницы "Лента заказов"'):
            wait_locator.wait_header_order_feed()

        with allure.step('Определяем номер заказа в блоке «В работе»"'):
            wait_locator.wait_disappear_message()
            number_in_working = uses_text.get_number_in_working()

            assert our_order_number == number_in_working

        # with allure.step('Определяем что наш номер заказа в блоке «Готовы появился»"'):
        #     number_are_ready = wait_locator.
        #
        # with allure.step('Нажимаем кнопку "Конструктор"'):
        #     click_locator.move_bun_to_basket()
        #
        # with allure.step('Нажимаем кнопку "Оформить заказ"'):
        #     click_locator.move_bun_to_basket()
        #
        # with allure.step('Ожидаем в окне "идентификатор заказа" номер нашего заказа'):
        #     click_locator.move_bun_to_basket()
        #
        # with allure.step('Закрываем окно "идентификатор заказа"'):
        #     click_locator.move_bun_to_basket()
        #
        # with allure.step('Нажимаем кнопку "Лента заказов"'):
        #     click_locator.move_bun_to_basket()
