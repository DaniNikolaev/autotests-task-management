from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.image import Image


class AttachmentCardComponent(BaseComponent):
    def __init__(self, page: Page, index: int = 0):
        super().__init__(page)
        self.index = index

        self.image = Image(page, "attachment-card-image",
                           "Attachment card image")
        self.name = Text(page, "attachment-card-name",
                         "Attachment card name")
        self.date = Text(page, "attachment-card-date",
                         "Attachment card date")
        self.download_button = Button(page, "download-attachment-button",
                                     "Attachment card download button")
        self.delete_button = Button(page, "delete-attachment-button",
                                   "Attachment card delete button")

    def check_card(self, data: dict | None = None):
        self.image.check_visible(nth=self.index)

        self.name.check_visible(nth=self.index)
        self.name.check_have_text(data['name'], nth=self.index)

        self.date.check_visible(nth=self.index)
        self.date.check_have_text(data['date'], nth=self.index)

    def check_download_button(self):
        self.download_button.check_visible(nth=self.index)
        self.download_button.check_enabled(nth=self.index)

    def check_delete_button(self):
        self.delete_button.check_visible(nth=self.index)
        self.delete_button.check_enabled(nth=self.index)

    def click_download_button(self):
        self.download_button.click(nth=self.index)

    def click_delete_button(self):
        self.delete_button.click(nth=self.index)

    def check_attachment(self, data: dict | None = None):
        self.check_card(data)
        self.check_download_button()
        self.check_delete_button()
