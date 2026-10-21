from typing import List

from playwright.sync_api import Page, Locator

from api.clients.projects.projects_schema import ProjectSchema
from ui.components.navbar_component import NavbarComponent
from ui.components.tasks.task_card_component import TaskCardComponent
from ui.components.tasks.task_form_component import TaskFormComponent
from ui.elements.Text import Text
from ui.elements.button import Button
from ui.elements.link import Link
from ui.pages.base_page import BasePage


class ProjectPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.back_link = Link(page, "back-to-projects-link",
                              "Project page back link")
        self.title = Text(page, "project-title",
                          "Project page title")
        self.edit_button = Button(page, "edit-project-button",
                                  "Project page edit button")
        self.delete_button = Button(page, "delete-project-button",
                                   "Project page delete button")
        self.description = Text(page, "project-description",
                               "Project page description")
        self.owner = Text(page, "project-owner",
                          "Project page owner")
        self.date_created = Text(page, "project-date-created",
                                 "Project page date created")

        self.tasks_title = Text(page, "tasks-title",
                               "Project page tasks title")
        self.create_task_button = Button(page, "create-task-button",
                                        "Project page create task button")
        self.create_task_form = TaskFormComponent(page, mode='create')
        self.edit_task_form = TaskFormComponent(page, mode='edit')

    @property
    def _all_tasks_cards(self) -> Locator:
        return self.page.get_by_test_id("task-card")

    def task_card_by_title(self, title: str) -> TaskCardComponent:
        card_locator = self._all_tasks_cards.filter(has_text=title)
        card_locator.first.wait_for(state="visible")
        return TaskCardComponent(self.page, locator=card_locator.first)

    @property
    def tasks_cards(self) -> List[TaskCardComponent]:
        count = self._all_tasks_cards.count()
        return [TaskCardComponent(self.page, index=i) for i in range(count)]

    def check_back_link(self):
        self.back_link.check_visible()
        self.back_link.check_have_attribute("href", "/projects")
        self.back_link.check_have_text("← Назад к проектам")

    def click_back_link(self):
        self.back_link.click()

    def check_title(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

    def check_description(self, description: str):
        self.description.check_visible()
        self.description.check_have_text(description)

    def check_owner(self, owner: str):
        self.owner.check_visible()
        self.owner.check_have_text(owner)

    def check_date_created(self, date_created: str):
        self.date_created.check_visible()
        self.date_created.check_have_text(date_created)

    def check_entire_project(self, project: ProjectSchema):
        self.check_title(project.title)
        self.check_description(project.description)
        self.check_owner(project.owner_user_id)
        self.check_date_created(project.created_at)

    def chek_title_and_description_project(self, project: ProjectSchema):
        self.check_title(project.title)
        self.check_description(project.description)

    def check_edit_button(self):
        self.edit_button.check_visible()
        self.edit_button.check_enabled()

    def click_edit_button(self):
        self.edit_button.click()

    def check_delete_button(self):
        self.delete_button.check_visible()
        self.delete_button.check_enabled()

    def check_tasks_title(self):
        self.tasks_title.check_visible()
        self.tasks_title.check_have_text(f"Задачи ({self._all_tasks_cards.count()})")

    def check_create_task_button(self):
        self.create_task_button.check_visible()
        self.create_task_button.check_enabled()

    def click_create_task_button(self):
        self.create_task_button.click()

    def check_tasks_cards(self):
        for card in self.tasks_cards:
            card.check_card()
            card.check_attachments_button()
            card.check_comments_button()
            card.check_edit_button()
            card.check_delete_button()
            