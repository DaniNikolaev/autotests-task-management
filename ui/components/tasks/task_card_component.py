from typing import Optional

from playwright.sync_api import Page, Locator

from api.clients.tasks.tasks_schema import TaskSchema
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class TaskCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0, locator: Optional[Locator] = None):
        super().__init__(page)

        if locator:
            self.root = locator
        else:
            self.root = self.page.get_by_test_id("task-card").nth(index)

        self.index = index
        self.title = Text(self.root, f"card-task-title",
                          f"Task card title")
        self.attachments_button = Button(self.root, f"card-task-attachments-button",
                                        f"Task card attachments button")
        self.comments_button = Button(self.root, f"card-task-comments-button",
                                     f"Task card comments button")
        self.edit_button = Button(self.root, f"card-task-edit-button",
                                 f"Task card edit button")
        self.delete_button = Button(self.root, f"card-task-delete-button",
                                   f"Task card delete button")
        self.status = Text(self.root, f"card-task-status",
                          f"Task card status")
        self.description = Text(self.root, f"card-task-description",
                               f"Task card description")
        self.priority = Text(self.root, f"card-task-priority",
                            f"Task card priority")
        self.estimated_time = Text(self.root, f"card-task-estimated-time",
                                  f"Task card estimated time")

    def check_attachments_button(self):
        self.attachments_button.check_visible()
        self.attachments_button.check_enabled()

    def click_attachments_button(self):
        self.attachments_button.click()

    def check_comments_button(self):
        self.comments_button.check_visible()
        self.comments_button.check_enabled()

    def click_comments_button(self):
        self.comments_button.click()

    def check_edit_button(self):
        self.edit_button.check_visible()
        self.edit_button.check_enabled()

    def click_edit_button(self):
        self.edit_button.click()

    def check_delete_button(self):
        self.delete_button.check_visible()
        self.delete_button.check_enabled()

    def click_delete_button(self):
        self.delete_button.click()

    def check_card(self, data: TaskSchema):
        self.title.check_visible()
        self.title.check_have_text(data.title)

        self.status.check_visible()
        self.status.check_have_attribute("data-value", data.status)

        self.description.check_visible()
        self.description.check_have_text(data.description)

        self.priority.check_visible()
        self.priority.check_have_attribute("data-value", data.priority)

        self.estimated_time.check_visible()
        self.estimated_time.check_have_text(data.estimated_time)

        self.check_attachments_button()
        self.check_comments_button()
        self.check_edit_button()
        self.check_delete_button()
