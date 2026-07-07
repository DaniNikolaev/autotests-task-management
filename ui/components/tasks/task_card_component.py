from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class TaskCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int):
        super().__init__(page)

        self.index = index
        self.title = Text(page, f"task-title",
                          f"Task card title")
        self.attachments_button = Button(page, f"task-card-attachments-button",
                                        f"Task card attachments button")
        self.comments_button = Button(page, f"task-card-comments-button",
                                     f"Task card comments button")
        self.edit_button = Button(page, f"task-card-edit-button",
                                 f"Task card edit button")
        self.delete_button = Button(page, f"task-card-delete-button",
                                   f"Task card delete button")
        self.status = Text(page, f"task-card-status",
                          f"Task card status")
        self.description = Text(page, f"task-card-description",
                               f"Task card description")
        self.priority = Text(page, f"task-card-priority",
                            f"Task card priority")
        self.estimated_time = Text(page, f"task-card-estimated-time",
                                  f"Task card estimated time")

    def check_attachments_button(self):
        self.attachments_button.check_visible(nth=self.index)
        self.attachments_button.check_enabled(nth=self.index)

    def click_attachments_button(self):
        self.attachments_button.click(nth=self.index)

    def check_comments_button(self):
        self.comments_button.check_visible(nth=self.index)
        self.comments_button.check_enabled(nth=self.index)

    def click_comments_button(self):
        self.comments_button.click(nth=self.index)

    def check_edit_button(self):
        self.attachments_button.check_visible(nth=self.index)
        self.attachments_button.check_enabled(nth=self.index)

    def click_edit_button(self):
        self.attachments_button.click(nth=self.index)

    def check_delete_button(self):
        self.delete_button.check_visible(nth=self.index)
        self.delete_button.check_enabled(nth=self.index)

    def click_delete_button(self):
        self.delete_button.click(nth=self.index)

    def check_card(self, data: dict | None = None):
        self.title.check_visible(nth=self.index)
        self.title.check_have_text(data['title'], nth=self.index)

        self.status.check_visible(nth=self.index)
        self.status.check_have_text(data['status'], nth=self.index)

        self.description.check_visible(nth=self.index)
        self.description.check_have_text(data['description'], nth=self.index)

        self.priority.check_visible(nth=self.index)
        self.priority.check_have_text(data['priority'], nth=self.index)

        self.estimated_time.check_visible(nth=self.index)
        self.estimated_time.check_have_text(data['estimated_time'], nth=self.index)
