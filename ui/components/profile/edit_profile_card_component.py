from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.button import Button
from ui.elements.input import Input


class EditProfileCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = Input(page, "first-name-input", "First name input")
        self.last_name_input = Input(page, "last-name-input", "Last name input")
        self.email_input = Input(page, "email-input", "Email input")
        self.cancel_button = Button(page, "cancel-button", "Cancel button")
        self.submit_button = Button(page, "submit-button", "Submit button")

    def check_first_name(self, first_name: str | None = None):
        self.first_name_input.check_visible()
        if first_name:
            self.first_name_input.check_have_text(first_name)

    def check_last_name(self, last_name: str | None = None):
        self.last_name_input.check_visible()
        if last_name:
            self.last_name_input.check_have_text(last_name)

    def check_email(self, email: str | None = None):
        self.email_input.check_visible()
        if email:
            self.email_input.check_have_text(email)

    def check_cancel_button(self):
        self.cancel_button.check_visible()
        self.cancel_button.check_enabled()
        self.cancel_button.check_have_text("Отмена")

    def check_submit_button(self):
        self.submit_button.check_visible()
        self.submit_button.check_enabled()
        self.submit_button.check_have_text("Сохранить")

    def check_edit_profile(self, data: dict | None = None):
        self.check_first_name(data['first_name'])
        self.check_last_name(data['last_name'])
        self.check_email(data['email'])
        self.check_cancel_button()
        self.check_submit_button()

    def fill_first_name(self, first_name: str):
        self.first_name_input.fill(first_name)

    def fill_last_name(self, last_name: str):
        self.last_name_input.fill(last_name)

    def fill_email(self, email: str):
        self.email_input.fill(email)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_submit_button(self):
        self.submit_button.click()

    def fill_edit_profile(self, data: dict | None = None):
        self.fill_first_name(data['first_name'])
        self.fill_last_name(data['last_name'])
        self.fill_email(data['email'])
