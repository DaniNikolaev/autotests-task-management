from typing import List

from playwright.sync_api import Page, Locator

from api.clients.comments.comments_schema import CommentSchema
from tools.api.fakers import fake
from ui.components.base_component import BaseComponent
from ui.components.comments.comment_card_component import CommentCardComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.textarea import Textarea


class CommentsComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "comments-title", "Comments title")
        self.comment_card = CommentCardComponent(page, index=0)
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

    def check_comments_title(self):
        self.title.check_visible()
        self.title.check_have_text(f"Комментарии ({self._all_comments_cards.count()})")

    def check_comments_cards(self, data: List[dict] | None = None):
        for index, card in enumerate(self.comments_cards):
            card.check_comment(data[index])

    def check_new_comment_textarea(self, text: str | None = None):
        self.new_comment_textarea.check_visible()
        if text is None:
            self.new_comment_textarea.check_have_placeholder("Напишите комментарий...")
        else:
            self.new_comment_textarea.check_have_text(text)

    def check_submit_comment_button(self):
        self.submit_comment_button.check_visible()
        self.submit_comment_button.check_enabled()
        self.submit_comment_button.check_have_text("Отправить")

    def click_submit_comment_button(self):
        self.submit_comment_button.click()

    def fill_new_comment_textarea(self, comment: CommentSchema | None = None):
        if comment is None:
            comment = CommentSchema(**fake.comment())
        self.new_comment_textarea.fill(comment.content)
        return comment
