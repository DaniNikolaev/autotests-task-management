from typing import List

import allure
import pytest

from api.clients.projects.projects_schema import ProjectSchema
from api.clients.tasks.tasks_schema import TaskSchema
from ui.pages.projects.project_page import ProjectPage


@pytest.mark.tasks
@pytest.mark.regression
@pytest.mark.ui
class TestTasks:
    @allure.title("Test successful tasks creation with empty tasks list")
    def test_successful_task_creation_with_empty_task_list(self,
                                                           project_page_with_auth: ProjectPage,
                                                           created_project: ProjectSchema):
        project_page_with_auth.check_back_link()
        project_page_with_auth.chek_title_and_description_project(created_project)
        project_page_with_auth.check_edit_button()
        project_page_with_auth.check_delete_button()
        project_page_with_auth.check_tasks_title()
        project_page_with_auth.check_create_task_button()
        project_page_with_auth.click_create_task_button()
        project_page_with_auth.create_task_form.check_task_form()
        data = project_page_with_auth.create_task_form.fill_task_form()
        project_page_with_auth.create_task_form.check_task_form(data)
        project_page_with_auth.create_task_form.click_submit_button()
        project_page_with_auth.check_current_url(f"/projects/{created_project.id}")
        task_card = project_page_with_auth.task_card_by_title(data.title)
        task_card.check_card(data)

    @allure.title("Test successful tasks creation with not empty tasks list")
    def test_successful_task_creation_with_not_empty_task_list(self,
                                                           project_page_with_tasks: ProjectPage,
                                                           created_project: ProjectSchema):
        project_page_with_tasks.click_create_task_button()
        project_page_with_tasks.create_task_form.check_task_form()
        data = project_page_with_tasks.create_task_form.fill_task_form()
        project_page_with_tasks.create_task_form.check_task_form(data)
        project_page_with_tasks.create_task_form.click_submit_button()
        project_page_with_tasks.check_current_url(f"/projects/{created_project.id}")
        task_card = project_page_with_tasks.task_card_by_title(data.title)
        task_card.check_card(data)

    @allure.title("Test all tasks data after creation new task")
    def test_all_tasks_data_after_creation_new_task(self,
                                                          project_page_with_tasks: ProjectPage,
                                                          created_project: ProjectSchema,
                                                          created_tasks_for_project: List[TaskSchema]
                                                          ):
        project_page_with_tasks.click_create_task_button()
        data = project_page_with_tasks.create_task_form.fill_task_form()
        project_page_with_tasks.create_task_form.click_submit_button()
        project_page_with_tasks.check_current_url(f"/projects/{created_project.id}")
        _ = project_page_with_tasks.task_card_by_title(data.title)
        all_tasks = created_tasks_for_project + [data]
        project_page_with_tasks.check_tasks_cards(all_tasks)


    @allure.title("Test successful task editing after creation")
    def test_successful_task_editing_after_creation(self,
                                                    project_page_with_auth: ProjectPage,
                                                    created_project: ProjectSchema):
        project_page_with_auth.click_create_task_button()
        project_page_with_auth.create_task_form.check_task_form()
        data = project_page_with_auth.create_task_form.fill_task_form()
        project_page_with_auth.create_task_form.click_submit_button()
        task_card = project_page_with_auth.task_card_by_title(data.title)
        project_page_with_auth.check_current_url(f"/projects/{created_project.id}")
        task_card.click_edit_button()
        project_page_with_auth.edit_task_form.check_task_form(data)
        data = project_page_with_auth.edit_task_form.fill_task_form()
        project_page_with_auth.edit_task_form.check_task_form(data)
        project_page_with_auth.edit_task_form.click_submit_button()
        task_card = project_page_with_auth.task_card_by_title(data.title)
        project_page_with_auth.check_current_url(f"/projects/{created_project.id}")
        task_card.check_card(data)
