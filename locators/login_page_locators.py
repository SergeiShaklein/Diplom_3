from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Кнопка "Войти" в форме Вход
    button_entrance_in_login_page = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Поле "Email" в окне "Вход"
    field_email = (By.XPATH, '//label[text()="Email"]/following-sibling::input')

    # Поле "Пароль" в окне "Вход"
    field_password = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')