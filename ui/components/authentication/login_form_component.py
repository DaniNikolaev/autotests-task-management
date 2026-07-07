from playwright.sync_api import Page

from tools.logger import get_logger
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input

logger = get_logger("LOGIN_FORM_COMPONENT")


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_label = Text(page, "login-email-label", "Email label")
        self.email_input = Input(page, "login-email-input", "Email input")

        self.password_label = Text(page, "login-password-label", "Password label")
        self.password_input = Input(page, "login-password-input", "Password input")

        self.login_button = Button(page, "login-button", "Login button")

    def click_login_button(self):
        self.login_button.click()

    def check_login_button(self):
        self.login_button.check_visible()
        self.login_button.check_enabled()
        self.login_button.check_have_text("Войти")

    def check_form(self, data: dict | None = None):
        self.email_label.check_visible()
        self.email_label.check_have_text("Email")

        self.password_label.check_visible()
        self.password_label.check_have_text("Пароль")

        if data is not None:
            self.email_input.check_visible()
            self.email_input.check_have_value(data['email'])

            self.password_input.check_visible()
            self.password_input.check_have_value(data['password'])

    def fill_form(self, data: dict):
        if data is not None:
            self.email_input.fill(data['email'])
            self.password_input.fill(data['password'])
