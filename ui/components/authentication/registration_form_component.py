from playwright.sync_api import Page

from tools.logger import get_logger
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input
from ui.elements.link import Link

logger = get_logger("REGISTRATION_FORM_COMPONENT")


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "register-email-input", "Email input")
        self.password_input = Input(page, "register-password-input", "Password input")
        self.first_name_input = Input(page, "register-firstname-input", "First name input")
        self.last_name_input = Input(page, "register-lastname-input", "Last name input")
        self.registration_button = Button(page, "register-button", "Registration button")
        self.error_message = Text(page, "register-error-message", "Registration page error message")

    def check_email_input(self, email: str | None = None):
        self.email_input.check_visible()
        if email:
            self.email_input.check_have_value(email)

    def check_password_input(self, password: str | None = None):
        self.password_input.check_visible()
        if password:
            self.password_input.check_have_value(password)

    def check_first_name_input(self, first_name: str | None = None):
        self.first_name_input.check_visible()
        if first_name:
            self.first_name_input.check_have_value(first_name)

    def check_last_name_input(self, last_name: str | None = None):
        self.last_name_input.check_visible()
        if last_name:
            self.last_name_input.check_have_value(last_name)

    def check_registration_button(self):
        self.registration_button.check_visible()
        self.registration_button.check_enabled()
        self.registration_button.check_have_text("Зарегистрироваться")

    def check_form(self, data: dict | None = None):
        if data is not None:
            self.check_email_input(data['email'])
            self.check_password_input(data['password'])
            self.check_first_name_input(data['first_name'])
            self.check_last_name_input(data['last_name'])
            self.check_registration_button()

    def check_error_message(self, email: str | None = None):
        self.error_message.check_visible()
        if email:
            self.error_message.check_have_text(f"User with email {email} already exists")

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def fill_password(self, password: str):
        self.password_input.fill(password)

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def click_registration_button(self):
        self.registration_button.click()

    def fill_form(self, data: dict):
        if data is not None:
            self.fill_email(data['email'])
            self.fill_password(data['password'])
            self.fill_first_name(data['first_name'])
            self.fill_last_name(data['last_name'])
