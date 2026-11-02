from playwright.sync_api import Page
from pydantic import FilePath

from api.clients.attachments.attachments_schema import AttachmentSchema, CreateAttachmentRequestSchema
from tools.api.fakers import fake
from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.file_input import FileInput
from ui.elements.input import Input


class UploadAttachmentComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.close_button = Button(page, "close-upload-model-button",
                                   "Upload attachment close button")
        self.file_input = FileInput(page, "upload-attachment-file-input",
                                   "Upload attachment file input")
        self.file_name_input = Input(page, "upload-attachment-filename-input",
                                   "Upload attachment upload button")
        self.file_directory_input = Input(page, "upload-attachment-file-directory-input",
                                       "Upload attachment file directory input")
        self.cancel_button = Button(page, "upload-attachment-cancel-button",
                                   "Upload attachment cancel button")
        self.upload_button = Button(page, "upload-attachment-upload-button",
                                   "Upload attachment upload button")

    def check_file_input(self):
        self.file_input.check_visible()

    def check_file_name_input(self, file_name: str | None = None):
        self.file_name_input.check_visible()
        if file_name:
            self.file_name_input.check_have_value(file_name)
        else:
            self.file_name_input.check_have_placeholder("Оставьте пустым для использования имени файла")

    def check_file_directory_input(self, directory: str | None = None):
        self.file_directory_input.check_visible()
        if directory:
            self.file_directory_input.check_have_value(directory)
        else:
            self.file_directory_input.check_have_placeholder("Например: documents, images")

    def check_cancel_button(self):
        self.cancel_button.check_visible()
        self.cancel_button.check_enabled()
        self.cancel_button.check_have_text("Отмена")

    def click_cancel_button(self):
        self.cancel_button.click()

    def check_upload_button(self, is_uploaded : bool = False):
        self.upload_button.check_visible()
        if is_uploaded:
            self.upload_button.check_enabled()
        else:
            self.upload_button.check_disabled()
        self.upload_button.check_have_text("Загрузить")

    def click_upload_button(self):
        self.upload_button.click()

    def check_upload_attachment(self, data: AttachmentSchema | None = None):
        self.check_file_input()
        if data:
            self.check_file_name_input(data.filename)
            self.check_file_directory_input(data.directory)
            self.check_upload_button(is_uploaded=True)
        else:
            self.check_file_name_input()
            self.check_file_directory_input()
            self.check_upload_button(is_uploaded=False)
        self.check_cancel_button()

    def upload_attachment(self, file_path: FilePath):
        #self.click_upload_button()
        self.file_input.set_input_files(str(file_path))

    def fill_file_name(self, file_name: str):
        self.file_name_input.fill(file_name)

    def fill_file_directory(self, file_directory: str):
        self.file_directory_input.fill(file_directory)

    def fill_upload_attachment(self, attachment: CreateAttachmentRequestSchema | None = None):
        if attachment is None:
            attachment = CreateAttachmentRequestSchema()
        self.upload_attachment(attachment.upload_file)
        self.fill_file_name(attachment.filename)
        self.fill_file_directory(attachment.directory)
        return attachment
