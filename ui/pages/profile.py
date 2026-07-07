from playwright.sync_api import Page

from ui.components.navbar_component import NavbarComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title = Text(page, "profile-title",
                          "Profile page title")
        self.edit_button = Button(page, "profile-edit-button",
                                  "Profile page edit button")
        self.profile_card = ProfileCardComponent(page)