from typing import List

from playwright.sync_api import Page, Locator

from ui.components.navbar_component import NavbarComponent
from ui.components.projects.project_card_component import ProjectCardComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.pages.base_page import BasePage


class ProjectsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.title = Text(page, "projects-title", "Projects page title")
        self.create_project_button = Button(page, "create-project-button",
                                            "Projects page create project button")

    @property
    def _all_projects_cards(self) -> Locator:
        return self.page.get_by_test_id("project-card")

    @property
    def projects_cards(self) -> List[ProjectCardComponent]:
        count = self._all_projects_cards.count()
        return [ProjectCardComponent(self.page, index=i) for i in range(count)]

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Проекты")

    def check_create_project_button(self):
        self.create_project_button.check_visible()
        self.create_project_button.check_enabled()

    def click_create_project_button(self):
        self.create_project_button.click()

    def check_projects_cards(self):
        for card in self.projects_cards:
            card.check_card()
            card.check_edit_button()
            card.check_delete_button()
