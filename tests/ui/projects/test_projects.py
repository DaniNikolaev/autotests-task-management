from typing import List

import allure
import pytest

from api.clients.projects.projects_schema import ProjectSchema
from ui.pages.projects.projects_page import ProjectsPage


@pytest.mark.projects
@pytest.mark.regression
@pytest.mark.ui
class TestProjects:
    @allure.title("Test successful project creation with empty projects list")
    def test_successful_project_creation_with_empty_projects_list(self, projects_page_with_auth: ProjectsPage):
        projects_page_with_auth.check_title()
        projects_page_with_auth.check_create_project_button()
        projects_page_with_auth.click_create_project_button()
        projects_page_with_auth.create_project_form.check_project_form()
        data = projects_page_with_auth.create_project_form.fill_project_form()
        projects_page_with_auth.create_project_form.check_project_form(data)
        projects_page_with_auth.create_project_form.click_submit_button()
        projects_page_with_auth.check_current_url("/projects")
        project_card = projects_page_with_auth.project_card_by_title(data.title)
        project_card.check_title_and_description_card(data)


    @allure.title("Test successful project creation with not empty projects list")
    def test_successful_project_creation_with_not_empty_projects_list(self, projects_page_with_data: ProjectsPage):
        projects_page_with_data.check_title()
        projects_page_with_data.check_create_project_button()
        projects_page_with_data.click_create_project_button()
        projects_page_with_data.create_project_form.check_project_form()
        data = projects_page_with_data.create_project_form.fill_project_form()
        projects_page_with_data.create_project_form.check_project_form(data)
        projects_page_with_data.create_project_form.click_submit_button()
        projects_page_with_data.check_current_url("/projects")
        project_card = projects_page_with_data.project_card_by_title(data.title)
        project_card.check_title_and_description_card(data)

    @allure.title("Test all projects data after creation new project")
    def test_all_projects_data_after_creation_new_project(self,
                                                          projects_page_with_data: ProjectsPage,
                                                          created_projects: List[ProjectSchema]
                                                          ):
        projects_page_with_data.click_create_project_button()
        data = projects_page_with_data.create_project_form.fill_project_form()
        projects_page_with_data.create_project_form.click_submit_button()
        projects_page_with_data.check_current_url("/projects")
        _ = projects_page_with_data.project_card_by_title(data.title)
        all_projects = created_projects + [data]
        projects_page_with_data.check_title_and_descriptions_projects_cards(all_projects)

    @allure.title("Test successful project editing after creation")
    def test_successful_project_editing_after_creation(self, projects_page_with_auth: ProjectsPage):
        projects_page_with_auth.click_create_project_button()
        projects_page_with_auth.create_project_form.check_project_form()
        data = projects_page_with_auth.create_project_form.fill_project_form()
        projects_page_with_auth.create_project_form.click_submit_button()
        project_card = projects_page_with_auth.project_card_by_title(data.title)
        projects_page_with_auth.check_current_url("/projects")
        project_card.click_edit_button()
        projects_page_with_auth.edit_project_form.check_project_form(data)
        data = projects_page_with_auth.edit_project_form.fill_project_form()
        projects_page_with_auth.edit_project_form.check_project_form(data)
        projects_page_with_auth.edit_project_form.click_submit_button()
        project_card = projects_page_with_auth.project_card_by_title(data.title)
        projects_page_with_auth.check_current_url("/projects")
        project_card.check_title_and_description_card(data)


