from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.components.comments.comments_component import CommentsComponent
from ui.elements.button import Button


class AttachmentsModalComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.comments_component = CommentsComponent(page)
        self.close_button = Button(page, "close-button", "Close button")

    def check_close_button(self):
        self.close_button.check_visible()
        self.close_button.check_enabled()
        self.close_button.check_have_text("Закрыть")