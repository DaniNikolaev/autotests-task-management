from playwright.sync_api import Page, expect

from tools.logger import get_logger
from ui.components.authentication.registration_form_component import RegistrationFormComponent
from ui.elements.Text import Text
from ui.elements.link import Link
from ui.pages.base_page import BasePage


logger = get_logger("REGISTRATION_PAGE")


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "register-title", "Registration page title")
        self.registration_form = RegistrationFormComponent(page)
        self.login_link = Link(page, "login-link", "Registration page login link")

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Регистрация")

    def check_login_link(self):
        self.login_link.check_visible()
        self.login_link.check_have_text("Войти")
        self.login_link.check_have_attribute("href", "/login")
