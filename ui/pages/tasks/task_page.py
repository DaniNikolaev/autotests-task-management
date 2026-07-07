from typing import List

from playwright.sync_api import Page, Locator

from ui.components.attachments.attachment_card_component import AttachmentCardComponent
from ui.components.comments.comment_card_component import CommentCardComponent
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
        self.back_link = Link(page, "back-link",
                              "Task page back link")
        self.title = Text(page, "task-title",
                          "Task page title")
        self.edit_button = Button(page, "edit-task-button",
                                  "Task page edit button")
        self.delete_button = Button(page, "delete-task-button",
                                    "Task page delete button")
        self.description = Text(page, "task-description",
                               "Task page description")
        self.status_label = Text(page, "task-status-label",
                                "Task page status label")
        self.status = Text(page, "task-status",
                          "Task page status")
        self.priority_label = Text(page, "task-priority-label",
                                  "Task page priority label")
        self.priority = Text(page, "task-priority",
                            "Task page priority")
        self.estimated_time_label = Text(page, "task-estimated-time-label",
                                        "Task page estimated time label")
        self.estimated_time = Text(page, "task-estimated-time",
                                  "Task page estimated time")
        self.project_label = Text(page, "task-project-label",
                                 "Task page project label")
        self.project = Text(page, "task-project",
                           "Task page project")
        self.created_label = Text(page, "task-created-label",
                                 "Task page created label")
        self.created = Text(page, "task-created",
                           "Task page created")
        self.updated_label = Text(page, "task-updated-label",
                                     "Task page updated label")
        self.updated = Text(page, "task-updated",
                                "Task page updated")

        self.comments_title = Text(page, "task-comments-title",
                                  "Task page comments title")
        self.attachments_title = Text(page, "task-attachments-title",
                                     "Task page attachments title")
        self.upload_attachments_button = Button(page, "upload-attachments-button",
                                              "Task page upload attachments button")

        self.new_comment_textarea = Textarea(page, "new-comment-textarea",
                                            "Task page new comment textarea")
        self.submit_comment_button = Button(page, "submit-comment-button",
                                           "Task page submit comment button")

    @property
    def _all_comments_cards(self) -> Locator:
        return self.page.get_by_test_id("comment-card")

    @property
    def comments_cards(self) -> List[CommentCardComponent]:
        count = self._all_comments_cards.count()
        return [CommentCardComponent(self.page, index=i) for i in range(count)]

    @property
    def _all_attachments_cards(self) -> Locator:
        return self.page.get_by_test_id("attachment-card")

    @property
    def attachments_cards(self) -> List[AttachmentCardComponent]:
        count = self._all_attachments_cards.count()
        return [AttachmentCardComponent(self.page, index=i) for i in range(count)]

    def check_back_link(self, project_id: str):
        self.back_link.check_visible()
        self.back_link.check_have_attribute("href", f"/project/{project_id}")
        self.back_link.check_have_text("Back")

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
        self.status_label.check_visible()
        self.status_label.check_have_text("Статус:")
        self.status.check_visible()
        self.status.check_have_text(status)

    def check_priority(self, priority: str):
        self.priority_label.check_visible()
        self.priority_label.check_have_text("Приоритет:")
        self.priority.check_visible()
        self.priority.check_have_text(priority)

    def check_estimated_time(self, estimated_time: str):
        self.estimated_time_label.check_visible()
        self.estimated_time_label.check_have_text("Оценка времени:")
        self.estimated_time.check_visible()
        self.estimated_time.check_have_text(estimated_time)

    def check_project(self, project: str):
        self.project_label.check_visible()
        self.project_label.check_have_text("Проект:")
        self.project.check_visible()
        self.project.check_have_text(project)

    def check_created(self, created: str):
        self.created_label.check_visible()
        self.created_label.check_have_text("Создано:")
        self.created.check_visible()
        self.created.check_have_text(created)

    def check_updated(self, updated: str):
        self.updated_label.check_visible()
        self.updated_label.check_have_text("Обновлено:")
        self.updated.check_visible()
        self.updated.check_have_text(updated)

    def check_comments_title(self):
        self.comments_title.check_visible()
        self.comments_title.check_have_text(f"Комментарии ({self._all_comments_cards.count()})")

    def check_attachments_title(self):
        self.attachments_title.check_visible()
        self.attachments_title.check_have_text(f"Вложения ({self._all_attachments_cards.count()})")

    def check_upload_attachments_button(self):
        self.upload_attachments_button.check_visible()
        self.upload_attachments_button.check_enabled()
        self.upload_attachments_button.check_have_text("Загрузить вложение")

    def check_comments_cards(self, data: dict | None = None):
        for card in self.comments_cards:
            card.check_card(data)
            card.check_edit_button()
            card.check_delete_button()

    def check_attachments_cards(self, data: dict | None = None):
        for card in self.attachments_cards:
            card.check_card(data)
            card.check_download_button()
            card.check_delete_button()

    def check_new_comment_textarea(self, text: str | None = None):
        self.new_comment_textarea.check_visible()
        if text is None:
            self.new_comment_textarea.check_have_attribute("placeholder",
                                                           "Напишите комментарий...")
        else:
            self.new_comment_textarea.check_have_text(text)

    def check_submit_comment_button(self):
        self.submit_comment_button.check_visible()
        self.submit_comment_button.check_enabled()
        self.submit_comment_button.check_have_text("Отправить")
