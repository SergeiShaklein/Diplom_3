from selenium.webdriver.common.by import By
class Locators:

    # -- Локаторы Авторизации --
    ###########################################################################
    # Кнопка "Войти в аккаунт" на главной
    button_entrance_account = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Кнопка "Войти" в форме Вход
    button_entrance_in_login_page = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Поле "Email" в окне "Вход"
    field_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" в окне "Вход"
    field_password = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')


    # -- Локаторы Личного Кабинета --
    ##############################################################################
    # Кнопка "Личный кабинет"
    button_private_area = (By.XPATH, '//p[text()="Личный Кабинет"]')


    # -- Локаторы Конструктора
    ################################################################################

    # Заголовок "Соберите бургер"
    header_create_burger = (By.XPATH, '//h1[text()="Соберите бургер"]')

    # Линк "Конструктор"
    button_construction = (By.XPATH, '//p[text()="Конструктор"]')

    # Ингредиент "Краторная булка N-200i"
    ingredient_crater_bun = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')

    # Область корзины
    basket_area = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")

    # Счетчик ингредиента "Краторная булка N-200i"
    ingredient_counter = (By.XPATH, "//a[contains(@href,'/ingredient/61c0c5a71d1f82001bdaaa6c')]//p[@class='counter_counter__num__3nue1']")

    # Заголовок детального окна ингридиентов
    header_details_ingredient = (By.XPATH, '//h2[text()="Детали ингредиента"]')

    # Название ингредиента "Краторная булка N-200i" в детальном окне
    name_crater_bun = (By.XPATH, '//p[text()="Краторная булка N-200i"]')

    # Крестик для закрытия деталей ингредиента
    close_details_ingredient_button = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")

    # -- Локаторы Ленты заказов
    ################################################################################
    # Кнопка "Лента заказов"
    button_order_feed = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Заголовок "Лента заказов"
    header_order_feed = (By.XPATH, '//h1[text()="Лента заказов"]')

    # Кнопка "Оформить заказ"
    place_order = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    # Cчетчик "Выполнено за все время"
    counter_all_time = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за все время:']]")

    # Cчетчик "Выполнено за сегодня"
    counter_today = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за сегодня:']]")

    # Номер заказа в разделе "В работе"
    number_in_working = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li[1]")

    # Номер заказа в разделе "Готовы"
    number_in_ready = (By.XPATH, '//li[contains(@class, "text text_type_digits-default mb-2")]')

    # Текст "идентификатор заказа"
    identifier_order = (By.XPATH, '//p[text()="идентификатор заказа"]')

    # Номер сделанного заказа
    our_order_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    # Крестик для закрытия деталей ингредиента
    close_button_modal_window = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    # Перекрывающее окно с анимацией
    disappear_animation = (By.XPATH, '//img[@alt="loading animation"]')

    # Перекрывающее модальное окно
    disappear_modal_window = (By.XPATH, "//section[contains(@class, 'Modal_modal__P3_V5')]/div[@class='Modal_modal_overlay__x2ZCr']")
    # (By.XPATH, "//div[@class='Modal_modal_overlay__x2ZCr']")

    # Сообщение Все текущие заказы готовы!
    disappear_message = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')



