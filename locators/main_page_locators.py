from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка "Личный кабинет"
    button_private_area = (By.XPATH, '//p[text()="Личный Кабинет"]')

    # Заголовок "Соберите бургер"
    header_create_burger = (By.XPATH, '//h1[text()="Соберите бургер"]')

    # Кнопка "Конструктор"
    button_construction = (By.XPATH, '//p[text()="Конструктор"]')

    # Кнопка "Лента заказов"
    button_order_feed = (By.XPATH, '//p[text()="Лента Заказов"]')

    # Кнопка "Войти в аккаунт" на главной
    button_entrance_account = (By.XPATH, '//button[text()="Войти в аккаунт"]')

    # Кнопка "Оформить заказ"
    place_order = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

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

