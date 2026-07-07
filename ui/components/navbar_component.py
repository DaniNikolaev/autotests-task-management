from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.button import Button
from ui.elements.link import Link


class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.projects_link = Link(page, "projects-link", "Navbar projects link")
        self.profile_button = Button(page, "profile-link", "Navbar profile button")
        self.logout_button = Button(page, "logout-button", "Navbar logout button")

    def check_projects_link(self):
        self.projects_link.check_visible()
        self.projects_link.check_have_text("Task Management")
        self.projects_link.check_have_attribute("href", "/projects")

    def check_profile_button(self):
        self.profile_button.check_visible()
        self.profile_button.check_have_text("Профиль")

    def check_logout_button(self):
        self.logout_button.check_visible()
        self.logout_button.check_have_text("Выйти")

    def click_projects_link(self):
        self.projects_link.click()

    def click_profile_button(self):
        self.profile_button.click()

    def click_logout_button(self):
        self.logout_button.click()
