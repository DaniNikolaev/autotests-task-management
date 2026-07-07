from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class ProjectCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0):
        super().__init__(page)

        self.title = Text(page, "project-card-title",
                          "Project card name")
        self.edit_button = Button(page, "project-card-edit-button",
                                  "Project card edit button")
        self.delete_button = Button(page, "project-card-delete-button",
                                    "Project card delete button")
        self.description = Text(page, "project-card-description",
                                "Project card description")
        self.owner = Text(page, "project-card-owner",
                          "Project card owner")
        self.date_created = Text(page, "project-card-date-created",
                                 "Project card date created")
        self.index = index

    def check_card(self, data: dict | None = None):
        self.title.check_visible(nth=self.index)
        self.title.check_have_text(data['title'], nth=self.index)
        self.description.check_visible(nth=self.index)
        self.description.check_have_text(data['description'], nth=self.index)
        self.owner.check_visible(nth=self.index)
        self.owner.check_have_text(data['owner'], nth=self.index)
        self.date_created.check_visible(nth=self.index)
        self.date_created.check_have_text(data['date_created'], nth=self.index)

    def check_edit_button(self):
        self.edit_button.check_visible(nth=self.index)
        self.edit_button.check_enabled(nth=self.index)

    def check_delete_button(self):
        self.delete_button.check_visible(nth=self.index)
        self.delete_button.check_enabled(nth=self.index)

    def click_edit_button(self):
        self.edit_button.click(nth=self.index)

    def click_delete_button(self):
        self.delete_button.click(nth=self.index)
