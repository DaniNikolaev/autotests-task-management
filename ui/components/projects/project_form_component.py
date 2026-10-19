from typing import Literal

from playwright.sync_api import Page

from tools.api.fakers import fake
from ui.components.base_component import BaseComponent
from ui.elements.button import Button
from ui.elements.input import Input


class ProjectFormComponent(BaseComponent):
    def __init__(self, page: Page, mode: Literal['create', 'edit']):
        super().__init__(page)
        self.mode = mode

        self.title_input = Input(page, "project-title-input", "Project title input")
        self.description_input = Input(page, "project-description-input", "Project description input")
        self.cancel_button = Button(page, "project-cancel-button", "Project cancel button")
        self.submit_button = Button(page, f"{mode}-project-submit-button", f"Project {mode} submit button")

    def check_title_input(self, name: str | None):
        self.title_input.check_visible()
        if name:
            self.title_input.check_have_value(name)

    def check_description_input(self, description: str | None):
        self.description_input.check_visible()
        if description:
            self.description_input.check_have_value(description)

    def check_cancel_button(self):
        self.cancel_button.check_visible()
        self.cancel_button.check_enabled()
        self.cancel_button.check_have_text("Отмена")

    def check_submit_button(self):
        self.submit_button.check_visible()
        self.submit_button.check_enabled()
        if self.mode == 'create':
            self.submit_button.check_have_text("Создать")
        else:
            self.submit_button.check_have_text("Обновить")

    def check_project_form(self, data: dict | None = None):
        self.check_title_input(data['title'] if data else None)
        self.check_description_input(data['description'] if data else None)
        self.check_cancel_button()
        self.check_submit_button()

    def fill_title(self, name: str):
        self.title_input.fill(name)

    def fill_description(self, description: str):
        self.description_input.fill(description)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_submit_button(self):
        self.submit_button.click()

    def fill_project_form(self, data: dict | None = None) -> dict:
        if data is None:
            data = fake.project_form()
        self.fill_title(data['title'])
        self.fill_description(data['description'])
        return data
