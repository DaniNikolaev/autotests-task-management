from playwright.sync_api import Page

from tools.logger import get_logger
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input

logger = get_logger("REGISTRATION_FORM_COMPONENT")


class RegistrationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_label = Text(page, "register-email-label", "Email label")
        self.email_input = Input(page, "register-email-input", "Email input")

        self.password_label = Text(page, "register-password-label", "Password label")
        self.password_input = Input(page, "register-password-input", "Password input")

        self.first_name_label = Text(page, "register-firstname-label", "First name label")
        self.first_name_input = Input(page, "register-firstname-input", "First name input")

        self.last_name_label = Text(page, "register-lastname-label", "Last name label")
        self.last_name_input = Input(page, "register-lastname-input", "Last name input")

        self.registration_button = Button(page, "register-button", "Registration button")

    def click_registration_button(self):
        self.registration_button.click()

    def check_registration_button(self):
        self.registration_button.check_visible()
        self.registration_button.check_enabled()
        self.registration_button.check_have_text("Зарегистрироваться")

    def check_form(self, data: dict | None = None):
        self.email_label.check_visible()
        self.email_label.check_have_text("Email")

        self.password_label.check_visible()
        self.password_label.check_have_text("Пароль")

        self.first_name_label.check_visible()
        self.first_name_label.check_have_text("Имя")

        self.last_name_label.check_visible()
        self.last_name_label.check_have_text("Фамилия")

        if data is not None:
            self.email_input.check_visible()
            self.email_input.check_have_value(data['email'])

            self.password_input.check_visible()
            self.password_input.check_have_value(data['password'])

            self.first_name_input.check_visible()
            self.first_name_input.check_have_value(data['firstname'])

            self.last_name_input.check_visible()
            self.last_name_input.check_have_value(data['lastname'])

    def fill_form(self, data: dict):
        if data is not None:
            self.email_input.fill(data['email'])
            self.password_input.fill(data['password'])
            self.first_name_input.fill(data['firstname'])
            self.last_name_input.fill(data['lastname'])
