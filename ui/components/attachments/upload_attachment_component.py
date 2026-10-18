from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.file_input import FileInput


class UploadAttachmentComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "upload-attachment-title",
                          "Upload attachment title")
        self.close_button = Button(page, "upload-attachment-close-button",
                                   "Upload attachment close button")
        self.file_input = FileInput(page, "upload-attachment-file-input",
                                   "Upload attachment file input")
        self.file_name_input = Text(page, "upload-attachment-upload-button",
                                   "Upload attachment upload button")
        self.file_directory_input = Text(page, "upload-attachment-file-directory-input",
                                       "Upload attachment file directory input")
        self.cancel_button = Button(page, "upload-attachment-cancel-button",
                                   "Upload attachment cancel button")
        self.upload_button = Button(page, "upload-attachment-upload-button",
                                   "Upload attachment upload button")

    def check_title(self):
        self.title.check_visible()
        self.title.check_have_text("Загрузить вложение")

    def check_file_input(self):
        self.file_input.check_visible()
        self.file_input.check_have_text("Выберите файл")

    def check_file_name_input(self, file_name: str | None = None):
        self.file_name_input.check_visible()
        if file_name:
            self.file_name_input.check_have_text(file_name)
        else:
            self.file_name_input.check_have_placeholder("Оставьте пустым для использования имени файла")

    def check_file_directory_input(self, directory: str | None = None):
        self.file_directory_input.check_visible()
        if directory:
            self.file_directory_input.check_have_text(directory)
        else:
            self.file_directory_input.check_have_placeholder("Например: documents, images")

    def check_cancel_button(self):
        self.cancel_button.check_visible()
        self.cancel_button.check_enabled()
        self.cancel_button.check_have_text("Отмена")

    def click_cancel_button(self):
        self.cancel_button.click()

    def check_upload_button(self):
        self.upload_button.check_visible()
        self.upload_button.check_enabled()
        self.upload_button.check_have_text("Загрузить")

    def click_upload_button(self):
        self.upload_button.click()

    def check_upload_attachment(self, data: dict):
        self.check_title()
        self.check_file_input()
        self.check_file_name_input(data['file_name'])
        self.check_file_directory_input(data['file_directory'])
        self.check_cancel_button()
        self.check_upload_button()
