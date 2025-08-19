import allure

import data
import locators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BaseAction

class LoginPageAction(BaseAction):
    with allure.step ('Кликаем на кнопку "Войти"'):
        def click_button_entrance_in_login_page(self):
            locator = locators.login_page_locators.LoginPageLocators
            self.click_element(locator.button_entrance_in_login_page)

    with allure.step ('Заполняем поле "email"'):
        def fill_email(self):
            locator = locators.login_page_locators.LoginPageLocators
            self.fill_field(locator.field_email, data.Credantial.email)

    with allure.step ('Заполняем поле "password"'):
        def fill_password(self):
            locator = locators.login_page_locators.LoginPageLocators
            self.fill_field(locator.field_password, data.Credantial.password)
