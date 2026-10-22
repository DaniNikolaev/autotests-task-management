from datetime import datetime
from typing import List

from playwright.sync_api import Page, Locator

from ui.components.attachments.attachment_card_component import AttachmentCardComponent
from ui.components.attachments.attachments_component import AttachmentsComponent
from ui.components.comments.comment_card_component import CommentCardComponent
from ui.components.comments.comments_component import CommentsComponent
from ui.components.navbar_component import NavbarComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input
from ui.elements.link import Link
from ui.elements.textarea import Textarea
from ui.pages.base_page import BasePage


class TaskPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.back_link = Link(page, "back-to-project-link",
                              "Task page back link")
        self.title = Text(page, "task-title",
                          "Task page title")
        self.edit_button = Button(page, "task-edit-button",
                                  "Task page edit button")
        self.delete_button = Button(page, "task-delete-button",
                                    "Task page delete button")
        self.description = Text(page, "task-description",
                               "Task page description")
        self.status = Text(page, "task-status",
                          "Task page status")
        self.priority = Text(page, "task-priority",
                            "Task page priority")
        self.estimated_time = Text(page, "task-estimated-time",
                                  "Task page estimated time")
        self.project = Text(page, "task-project",
                           "Task page project")
        self.created = Text(page, "task-created",
                           "Task page created")
        self.updated = Text(page, "task-updated",
                                "Task page updated")
        self.comments = CommentsComponent(page)
        self.attachments = AttachmentsComponent(page)

    @property
    def _all_comments_cards(self) -> Locator:
        return self.page.get_by_test_id("comment-card")

    def comment_card_by_content(self, title: str) -> CommentCardComponent:
        card_locator = self._all_comments_cards.filter(has_text=title)
        card_locator.first.wait_for(state="visible")
        return CommentCardComponent(self.page, locator=card_locator.first)

    @property
    def comments_cards(self) -> List[CommentCardComponent]:
        count = self._all_comments_cards.count()
        return [CommentCardComponent(self.page, index=i) for i in range(count)]

    def check_back_link(self, project_id: str):
        self.back_link.check_visible()
        self.back_link.check_have_attribute("href", f"/projects/{project_id}")
        self.back_link.check_have_text("← Назад к проекту")

    def click_back_link(self):
        self.back_link.click()

    def check_edit_button(self):
        self.edit_button.check_visible()
        self.edit_button.check_enabled()
        self.edit_button.check_have_text("Редактировать")

    def check_delete_button(self):
        self.delete_button.check_visible()
        self.delete_button.check_enabled()
        self.delete_button.check_have_text("Удалить задачу")

    def click_edit_button(self):
        self.edit_button.click()

    def click_delete_button(self):
        self.delete_button.click()

    def check_title(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

    def check_description(self, description: str):
        self.description.check_visible()
        self.description.check_have_text(description)

    def check_status(self, status: str):
        self.status.check_visible()
        self.status.check_have_attribute("data-value", status)

    def check_priority(self, priority: str):
        self.priority.check_visible()
        self.priority.check_have_attribute("data-value", priority)

    def check_estimated_time(self, estimated_time: str):
        self.estimated_time.check_visible()
        self.estimated_time.check_have_text(estimated_time)

    def check_project(self, project: str):
        self.project.check_visible()
        self.project.check_have_text(project)

    def check_created(self, created_at: str | datetime):
        self.created.check_visible()
        if isinstance(created_at, datetime):
            expected_text = created_at.strftime("%d.%m.%Y")
        else:
            expected_text = created_at
        self.created.check_have_text(f"Создано: {expected_text}")

    def check_updated(self, updated_at: str | datetime | None):
        self.updated.check_visible()
        if isinstance(updated_at, datetime):
            expected_text = updated_at.strftime("%d.%m.%Y")
            self.created.check_have_text(f"Обновлено: {expected_text}")
        elif isinstance(updated_at, str):
            expected_text = updated_at
            self.created.check_have_text(f"Обновлено: {expected_text}")
