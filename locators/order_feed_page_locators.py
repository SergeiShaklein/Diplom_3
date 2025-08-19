from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    # Cчетчик "Выполнено за все время"
    counter_all_time = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за все время:']]")

    # Cчетчик "Выполнено за сегодня"
    counter_today = (By.XPATH, "//p[preceding-sibling::p[text()='Выполнено за сегодня:']]")

    # Номер заказа в разделе "В работе"
    number_in_working = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li[1]")

    # Номер сделанного заказа
    our_order_number = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')

    # Крестик для закрытия деталей ингредиента
    close_button_modal_window = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    # Перекрывающее окно с анимацией
    disappear_animation = (By.XPATH, '//img[@alt="loading animation"]')

    # Сообщение Все текущие заказы готовы!
    disappear_message = (By.XPATH, '//li[text()="Все текущие заказы готовы!"]')

    # Заголовок "Лента заказов"
    header_order_feed = (By.XPATH, '//h1[text()="Лента заказов"]')



