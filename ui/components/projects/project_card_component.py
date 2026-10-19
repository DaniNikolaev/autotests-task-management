from typing import Optional

from playwright.sync_api import Page, Locator

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class ProjectCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0, locator: Optional[Locator] = None):
        super().__init__(page)

        if locator:
            self.root = locator
        else:
            self.root = self.page.get_by_test_id("project-card").nth(index)

        self.title = Text(self.root, "project-card-title",
                          "Project card name")
        self.edit_button = Button(self.root, "project-card-edit-button",
                                  "Project card edit button")
        self.delete_button = Button(self.root, "project-card-delete-button",
                                    "Project card delete button")
        self.description = Text(self.root, "project-card-description",
                                "Project card description")
        self.owner = Text(page, "project-card-owner",
                          "Project card owner")
        self.date_created = Text(self.root, "project-card-date-created",
                                 "Project card date created")
        self.index = index

    def check_title(self, title):
        self.title.check_visible()
        self.title.check_have_text(title)

    def check_description(self, description: str):
        self.description.check_visible()
        self.description.check_have_text(description)

    def check_owner(self, owner: str):
        self.owner.check_visible()
        self.owner.check_have_text(owner)

    def check_date_created(self, date_created: str):
        self.date_created.check_visible()
        self.date_created.check_have_text(date_created)

    def check_card(self, data: dict | None = None):
        self.check_title(data['title'])
        self.check_description(data['description'])
        self.check_owner(data['owner'])
        self.check_date_created(data['date_created'])
        self.check_edit_button()
        self.check_delete_button()

    def check_edit_button(self):
        self.edit_button.check_visible()
        self.edit_button.check_enabled()

    def check_delete_button(self):
        self.delete_button.check_visible()
        self.delete_button.check_enabled()

    def click_edit_button(self):
        self.edit_button.click()

    def click_delete_button(self):
        self.delete_button.click()
