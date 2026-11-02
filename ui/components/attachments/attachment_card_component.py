from datetime import datetime
from typing import Optional

from playwright.sync_api import Page, Locator

from api.clients.attachments.attachments_schema import CreateAttachmentRequestSchema, AttachmentSchema
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.file_input import FileInput
from ui.elements.image import Image


class AttachmentCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0, locator: Optional[Locator] = None):
        super().__init__(page)

        if locator:
            self.root = locator
        else:
            self.root = self.page.get_by_test_id("attachment-card").nth(index)

        self.index = index

        self.name = Text(self.root, "attachment-card-name",
                         "Attachment card name")
        self.date = Text(self.root, "attachment-card-date",
                         "Attachment card date")
        self.download_button = Button(self.root, "attachment-card-download-button",
                                     "Attachment card download button")
        self.delete_button = Button(self.root, "attachment-card-delete-button",
                                   "Attachment card delete button")

    def check_name(self, name: str):
        self.name.check_visible()
        self.name.check_have_text(name)

    def check_created_at(self, created: datetime | str):
        self.date.check_visible()
        if isinstance(created, datetime):
            expected_text = created.strftime("%d.%m.%Y")
        else:
            expected_text = created
        self.date.check_have_text(expected_text)

    def check_card(self, data: AttachmentSchema):
        self.check_name(data.filename)
        self.check_created_at(data.created_at)
        self.check_download_button()
        self.check_delete_button()

    def check_download_button(self):
        self.download_button.check_visible()
        self.download_button.check_enabled()

    def check_delete_button(self):
        self.delete_button.check_visible()
        self.delete_button.check_enabled()

    def click_download_button(self):
        self.download_button.click()

    def click_delete_button(self):
        self.delete_button.click()
