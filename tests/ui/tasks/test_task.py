from typing import List

import allure
import pytest

from api.clients.comments.comments_schema import CommentSchema
from api.clients.projects.projects_schema import ProjectSchema
from api.clients.tasks.tasks_schema import TaskSchema
from ui.pages.tasks.task_page import TaskPage


@pytest.mark.task
@pytest.mark.regression
@pytest.mark.ui
class TestTask:
    @allure.title("Test task page")
    def test_task_page(self,
                       task_page_with_auth: TaskPage,
                       created_project: ProjectSchema,
                       created_task_for_project: TaskSchema):
        task_page_with_auth.check_back_link(created_project.id)
        task_page_with_auth.check_title(created_task_for_project.title)
        task_page_with_auth.check_edit_button()
        task_page_with_auth.check_delete_button()
        task_page_with_auth.check_description(created_task_for_project.description)
        task_page_with_auth.check_status(created_task_for_project.status)
        task_page_with_auth.check_priority(created_task_for_project.priority)
        task_page_with_auth.check_estimated_time(created_task_for_project.estimated_time)
        task_page_with_auth.check_project(created_project.title)
        task_page_with_auth.check_created(created_task_for_project.created_at)

    @allure.title("Test page create comment with empty comments list")
    def test_page_create_comment_with_empty_comments_list(self,
                            task_page_with_auth: TaskPage,
                            created_task_for_project: TaskSchema):
        task_page_with_auth.comments.check_comments_title()
        task_page_with_auth.comments.check_new_comment_textarea()
        data = task_page_with_auth.comments.fill_new_comment_textarea()
        task_page_with_auth.comments.check_submit_comment_button()
        task_page_with_auth.comments.click_submit_comment_button()
        task_page_with_auth.check_current_url(f"/tasks/{created_task_for_project.id}")
        task_page_with_auth.comments.check_comments_title()
        task_page_with_auth.comments.comment_card.check_content_and_date_card(data)

    @allure.title("Test page create comment with not empty comments list")
    def test_page_create_comment_with_not_empty_comments_list(self,
                            task_page_with_comments: TaskPage,
                            created_task_for_project: TaskSchema,
                            created_comments_for_tasks: List[CommentSchema]):
        task_page_with_comments.comments.check_comments_title()
        task_page_with_comments.comments.check_new_comment_textarea()
        data = task_page_with_comments.comments.fill_new_comment_textarea()
        task_page_with_comments.comments.check_submit_comment_button()
        task_page_with_comments.comments.click_submit_comment_button()
        task_page_with_comments.check_current_url(f"/tasks/{created_task_for_project.id}")
        task_page_with_comments.comments.check_comments_title()
        task_card = task_page_with_comments.comment_card_by_content(data.content)
        task_card.check_content_and_date_card(data)
