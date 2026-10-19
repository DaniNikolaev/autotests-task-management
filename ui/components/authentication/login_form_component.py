from playwright.sync_api import Page

from tools.logger import get_logger
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input
from ui.elements.link import Link

logger = get_logger("LOGIN_FORM_COMPONENT")


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "login-email-input", "Email input")
        self.password_input = Input(page, "login-password-input", "Password input")
        self.login_button = Button(page, "login-button", "Login button")
        self.error_message = Text(page, "login-error-message", "Login error message")

    def check_email_input(self, email: str | None = None):
        self.email_input.check_visible()
        if email:
            self.email_input.check_have_value(email)

    def check_password_input(self, password: str | None = None):
        self.password_input.check_visible()
        if password:
            self.password_input.check_have_value(password)

    def check_login_button(self):
        self.login_button.check_visible()
        self.login_button.check_enabled()
        self.login_button.check_have_text("Войти")

    def check_form(self, data: dict | None = None):
        if data is not None:
            self.check_email_input(data['email'])
            self.check_password_input(data['password'])
            self.check_login_button()

    def check_error_message(self):
        self.error_message.check_visible()
        self.error_message.check_have_text_from_list(["Неверный email или пароль", "Invalid credentials"])

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def fill_form(self, data: dict):
        if data is not None:
            self.fill_email(data['email'])
            self.fill_password(data['password'])

    def click_login_button(self):
        self.login_button.click()
        