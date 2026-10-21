from typing import List

from playwright.sync_api import Page, Locator, expect

from api.clients.projects.projects_schema import ProjectSchema
from ui.components.navbar_component import NavbarComponent
from ui.components.projects.project_card_component import ProjectCardComponent
from ui.components.projects.project_form_component import ProjectFormComponent
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
        self.create_project_form = ProjectFormComponent(page, mode="create")
        self.edit_project_form = ProjectFormComponent(page, mode="edit")

    @property
    def _all_projects_cards(self) -> Locator:
        return self.page.get_by_test_id("project-card")

    def project_card_by_title(self, title: str) -> ProjectCardComponent:
        card_locator = self._all_projects_cards.filter(has_text=title)
        card_locator.first.wait_for(state="visible")
        return ProjectCardComponent(self.page, locator=card_locator.first)

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

    def check_entire_projects_cards(self, data_list: List[dict]):
        for card, data in zip(self.projects_cards, data_list):
            card.check_entire_card(data)
            card.check_edit_button()
            card.check_delete_button()

    def check_title_and_descriptions_projects_cards(self, data_list: List[ProjectSchema]):
        actual_count = self._all_projects_cards.count()
        print(actual_count, len(data_list))
        assert actual_count == len(data_list)

        for data in data_list:
            title = data.title if hasattr(data, 'title') else data['title']
            card = self.project_card_by_title(title)
            card.check_title_and_description_card(data)
            card.check_edit_button()
            card.check_delete_button()