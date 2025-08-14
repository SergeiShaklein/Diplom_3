import allure
import helpers

@allure.feature('Функциональность раздела «Лента заказов»')
@allure.story ('Проверка функциональности счетчиков «Выполнено за всё время» и «Выполнено за сегодня», а также номера заказа в разделе «В работе»')

class TestCheckMainPage:

    @allure.title ('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
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

        with allure.step('Определяем количество выполенных заказов за всё время"'):
            wait_locator.wait_disappear_message()
            order_for_all_time = uses_text.get_value_all_time()

            assert our_order_number == order_for_all_time

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_counter_today(self, driver):
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
            # wait_locator.wait_disappear_modal_window()
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

        with allure.step('Определяем количество выполенных заказов сегодня"'):
            wait_locator.wait_disappear_message()
            last_order_for_today = uses_text.get_value_today()

        with allure.step('Кликаем на кнопку "Конструктор"'):
            click_locator.click_constructor()  # кликаем Конструктор
            driver.refresh()

        with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            click_locator.move_bun_to_basket()

        with allure.step('Нажимаем кнопку "Оформить заказ"'):
            # wait_locator.wait_disappear_modal_window()
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

        with allure.step('Определяем количество выполенных заказов сегодня"'):
            wait_locator.wait_disappear_message()
            excepted_order_for_today = uses_text.get_value_today()

            assert excepted_order_for_today > last_order_for_today



    @allure.title('Проверка, что при после оформления заказа его номер появляется в разделе «В работе»')
    def test_order_in_process(self, driver):
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
            # wait_locator.wait_disappear_modal_window()
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
