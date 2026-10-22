from datetime import datetime
from typing import Optional

from playwright.sync_api import Page, Locator

from api.clients.comments.comments_schema import CommentSchema
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class CommentCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0, locator: Optional[Locator] = None):
        super().__init__(page)

        if locator:
            self.root = locator
        else:
            self.root = self.page.get_by_test_id("comment-card").nth(index)

        self.index = index

        self.owner = Text(self.root, "comment-card-author",
                          "Comment card author")
        self.created_at = Text(self.root, "comment-card-date",
                               "Comment card date")
        self.text = Text(self.root, "comment-card-content",
                         "Comment card content")

        self.edit_button = Button(self.root, "comment-card-edit-button",
                                  "Comment card edit button")
        self.delete_button = Button(self.root, "comment-card-delete-button",
                                    "Comment card delete button")

    def check_entire_card(self, data: CommentSchema | None = None):
        self.owner.check_visible()
        self.owner.check_have_text(f"{data['firstname']} {data['lastname']}")
        self.created_at.check_visible()
        self.created_at.check_have_text(data['created_at'])
        self.text.check_visible()
        self.text.check_have_text(data['text'])

    def check_created_at(self, created: datetime | str):
        self.created_at.check_visible()
        if isinstance(created, datetime):
            expected_text = created.strftime("%d.%m.%Y")
        else:
            expected_text = created
        self.created_at.check_have_text(expected_text)

    def check_content(self, text: str):
        self.text.check_visible()
        self.text.check_have_text(text)

    def check_content_and_date_card(self, data: CommentSchema):
        self.check_created_at(data.created_at)
        self.check_content(data.content)

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

    def check_comment(self, data: CommentSchema | None = None):
        self.check_card(data)
        self.check_edit_button()
        self.check_delete_button()
