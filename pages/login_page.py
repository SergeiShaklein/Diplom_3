import data
import locators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BaseAction

class LoginPageAction(BaseAction):
    # Клик на кнопку "Войти"
    def click_button_entrance_in_login_page(self):
        locator = locators.login_page_locators.LoginPageLocators
        self.click_element(locator.button_entrance_in_login_page)

    # Заполнение поля email
    def fill_email(self):
        locator = locators.login_page_locators.LoginPageLocators
        self.fill_field(locator.field_email, data.Credantial.email)

    # Заполнение поля password
    def fill_password(self):
        locator = locators.login_page_locators.LoginPageLocators
        self.fill_field(locator.field_password, data.Credantial.password)
