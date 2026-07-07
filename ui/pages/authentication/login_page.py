from playwright.sync_api import Page

from ui.components.authentication.login_form_component import LoginFormComponent
from ui.elements.Text import Text
from ui.elements.link import Link
from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "login-title", "Login page title")
        self.login_form = LoginFormComponent(page)
        self.register_text = Text(page, "login-register-text", "Login page registration text")
        self.register_link = Link(page, "register-link", "Login page registration link")

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Вход")

    def check_register_text(self):
        self.register_text.check_visible()
        self.register_text.check_have_text("Нет аккаунта?")

    def check_register_link(self):
        self.register_link.check_visible()
        self.register_link.check_have_text("Зарегистрироваться")
        self.register_link.check_have_attribute("href", "/register")
