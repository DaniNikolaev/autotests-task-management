from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class CommentCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int):
        super().__init__(page)
        self.index = index

        self.owner = Text(page, "comment-card-owner",
                          "Comment card owner")
        self.created_at = Text(page, "comment-card-created",
                               "Comment card created")
        self.text = Text(page, "comment-card-text",
                         "Comment card text")

        self.edit_button = Button(page, "edit-comment-card-button",
                                  "Comment card edit button")
        self.delete_button = Button(page, "delete-comment-card-button",
                                    "Comment card delete button")

    def check_card(self, data: dict | None = None):
        self.owner.check_visible(nth=self.index)
        self.owner.check_have_text(f"{data['firstname']} {data['lastname']}", nth=self.index)
        self.created_at.check_visible(nth=self.index)
        self.created_at.check_have_text(data['created_at'], nth=self.index)
        self.text.check_visible(nth=self.index)
        self.text.check_have_text(data['text'], nth=self.index)

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
