from typing import Literal

from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.input import Input
from ui.elements.textarea import Textarea


class TaskFormComponent(BaseComponent):
    def __init__(self, page: Page, mode: Literal['create', 'edit']):
        super().__init__(page)

        self.mode = mode

        # 1. Заголовок модального окна (H3).
        # Так как у него нет data-testid, мы берем его строго внутри корневого элемента модалки.
        self.modal_heading = self.page.get_by_test_id(f"{mode}-task-modal").locator("h3")

        # 2. Поля формы (Общие для create и edit, так как сущности одни и те же)
        self.title_input = Input(page, "task-title-input", "Task title input")
        self.description_input = Input(page, "task-description-input", "Task description textarea")
        self.status_select = SelectOption(page, "task-status-select", "Task status select")
        self.priority_select = SelectOption(page, "task-priority-select", "Task priority select")
        self.estimated_time_input = Input(page, "task-estimated-time-input", "Task estimated time input")

        # 3. Общие элементы (Кнопка отмены и блок ошибки)
        self.cancel_button = Button(page, "task-cancel-button", "Task cancel button")
        self.error_message = Text(page, "task-error-message", "Task error message")

        # 4. Кнопка отправки (СТРОГО зависит от режима: create-task-submit-button или edit-task-submit-button)
        self.submit_button = Button(page, f"{mode}-task-submit-button", f"Task {mode} submit button")


    def check_title_input(self, name: str | None):
        self.title_input.check_visible()
        if name:
            self.title_input.check_have_text(name)

    def check_description_textarea(self, description: str | None):
        self.description_input.check_visible()
        if description:
            self.description_input.check_have_text(description)

    def check_status_select(self, status: str | None):
        self.status_select.check_visible()
        if status:
            self.status_select.check_have_text(status)

    def check_priority_select(self, priority: str | None):
        self.priority_select.check_visible()
        if priority:
            self.priority_select.check_have_text(priority)

    def check_estimated_time_input(self, estimated_time: str | None):
        self.estimated_time_input.check_visible()
        if estimated_time:
            self.estimated_time_input.check_have_text(estimated_time)

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


    def check_task_form(self, data: dict | None = None):
        self.check_title_input(data['name'])
        self.check_description_textarea(data['description'])
        self.check_status_select(data['status'])
        self.check_priority_select(data['priority'])
        self.check_estimated_time_input(data['estimated_time'])
        self.check_cancel_button()
        self.check_submit_button()

    def fill_name(self, name: str):
        self.title_input.fill(name)

    def fill_description(self, description: str):
        self.description_input.fill(description)

    def select_status(self, status: str):
        self.status_select.select(status)

    def select_priority(self, priority: str):
        self.priority_select.select(priority)

    def fill_estimated_time(self, estimated_time: str):
        self.estimated_time_input.fill(estimated_time)

    def click_cancel_button(self):
        self.cancel_button.click()

    def click_submit_button(self):
        self.submit_button.click()

    def fill_task_form(self, data: dict | None = None):
        self.fill_name(data['name'])
        self.fill_description(data['description'])
        self.select_status(data['status'])
        self.select_priority(data['priority'])
        self.fill_estimated_time(data['estimated_time'])
