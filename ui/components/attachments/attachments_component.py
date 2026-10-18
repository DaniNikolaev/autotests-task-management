from typing import List

from playwright.sync_api import Page, Locator

from ui.components.attachments.attachment_card_component import AttachmentCardComponent
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button


class AttachmentsComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "attachments-title", "Attachments title")
        self.upload_button = Button(page, "upload-button", "Attachments upload button")

    @property
    def _all_attachments_cards(self) -> Locator:
        return self.page.get_by_test_id("attachment-card")

    @property
    def attachments_cards(self) -> List[AttachmentCardComponent]:
        count = self._all_attachments_cards.count()
        return [AttachmentCardComponent(self.page, index=i) for i in range(count)]

    def check_attachments_title(self):
        self.title.check_visible()
        self.title.check_have_text(f"Вложения ({self._all_attachments_cards.count()})")

    def check_upload_attachments_button(self):
        self.upload_button.check_visible()
        self.upload_button.check_enabled()
        self.upload_button.check_have_text("Загрузить вложение")

    def check_attachments_cards(self, data: List[dict] | None = None):
        for index, card in enumerate(self.attachments_cards):
            card.check_attachment(data[index])
