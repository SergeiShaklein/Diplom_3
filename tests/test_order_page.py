import allure
from pages.main_page import MainPageAction
from pages.order_page import OrderPageAction
from pages.login_page import LoginPageAction

@allure.feature('Функциональность раздела «Лента заказов»')
@allure.story ('Проверка функциональности счетчиков «Выполнено за всё время» и «Выполнено за сегодня», а также номера заказа в разделе «В работе»')

class TestCheckOrderPage:

    @allure.title ('Проверка, что при создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_counter_all_time(self, driver):
        main_page = MainPageAction(driver)
        order_page = OrderPageAction(driver)
        login_page = LoginPageAction(driver)

        with allure.step('Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
            main_page.click_button_entrance_account()
            login_page.fill_email()
            login_page.fill_password()
            login_page.click_button_entrance_in_login_page()

        with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            main_page.move_bun_to_basket()

        with allure.step('Нажимаем кнопку "Оформить заказ"'):
            main_page.click_button_place_order()

        with allure.step('Ожидаем загрузки модульного окна с идентификатором заказа'):
            order_page.close_button_is_clickable()

        with allure.step('Определяем номер заказа в окне с идентификатором заказа'):
            order_page.wait_disappear_animation()
            our_order_number = order_page.get_our_order_number()

        with allure.step('Закрываем модульное окна с идентификатором заказа'):
            order_page.click_close_modal_window()

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Ожидаем загрузки страницы "Лента заказов"'):
            order_page.wait_header_order_feed()

        with allure.step('Определяем количество выполенных заказов за всё время"'):
            order_page.wait_disappear_message()
            order_for_all_time = order_page.get_value_all_time()

        with allure.step('Проверяем, что изначальное количество выполенных заказов "за всё время" увеличилось и равно порядковому номеру нашего заказа'):
            assert our_order_number == order_for_all_time

    @allure.title('Проверка, что при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_counter_today(self, driver):
        main_page = MainPageAction(driver)
        order_page = OrderPageAction(driver)
        login_page = LoginPageAction(driver)

        with allure.step('Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
            main_page.click_button_entrance_account()
            login_page.fill_email()
            login_page.fill_password()
            login_page.click_button_entrance_in_login_page()

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Ожидаем загрузки счетчика "Выполнено за сегодня"'):
            order_page.wait_counter_today()

        with allure.step('Определяем количество выполенных заказов сегодня"'):
            last_order_for_today = int(order_page.get_value_today())

        with allure.step('Кликаем на кнопку "Конструктор"'):
            main_page.click_constructor()

        with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            main_page.move_bun_to_basket()

        with allure.step('Нажимаем кнопку "Оформить заказ"'):
            main_page.click_button_place_order()

        with allure.step('Ожидаем загрузки модульного окна с идентификатором заказа'):
            order_page.close_button_is_clickable()

        with allure.step('Определяем номер заказа в окне с идентификатором заказа'):
            order_page.wait_disappear_animation()

        with allure.step('Закрываем модульное окна с идентификатором заказа'):
            order_page.click_close_modal_window()

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Ожидаем загрузки счетчик "Выполнено за сегодня"'):
            order_page.wait_counter_today()

        with allure.step('Определяем количество выполенных заказов сегодня"'):
            excepted_order_for_today = int(order_page.get_value_today())

        with allure.step('Проверяем, что изначальное количество выполенных заказов "за сегодня" увеличилось на одну единицу'):
            assert excepted_order_for_today == last_order_for_today + 1



    @allure.title('Проверка, что при после оформления заказа его номер появляется в разделе «В работе»')
    def test_order_in_process(self, driver):
        main_page = MainPageAction(driver)
        order_page = OrderPageAction(driver)
        login_page = LoginPageAction(driver)

        with allure.step('Авторизовываемся: Нажимаем кнопку "Войти в аккаунт", вводим email, пароль и кликаем кнопку "Войти"'):
            main_page.click_button_entrance_account()
            login_page.fill_email()
            login_page.fill_password()
            login_page.click_button_entrance_in_login_page()

        with allure.step('Перетаскиваем ингредиент "Краторная булка N-200i" в корзину'):
            main_page.move_bun_to_basket()

        with allure.step('Нажимаем кнопку "Оформить заказ"'):
            main_page.click_button_place_order()

        with allure.step('Ожидаем загрузки модульного окна с идентификатором заказа'):
            order_page.close_button_is_clickable()

        with allure.step('Определяем номер заказа в окне с идентификатором заказа'):
            our_order_number = order_page.get_our_order_number()

        with allure.step('Закрываем модульное окна с идентификатором заказа'):
            order_page.click_close_modal_window()

        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Ожидаем загрузки страницы "Лента заказов"'):
            order_page.wait_header_order_feed()

        with allure.step('Определяем номер заказа в блоке «В работе»"'):
            number_in_working = order_page.get_number_in_working()

        with allure.step('Проверяем, что в разделе «В работе» появился номер нашего заказа'):
            assert our_order_number == number_in_working
