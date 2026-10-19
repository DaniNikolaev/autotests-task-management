import allure
import pytest

from ui.pages.projects.projects_page import ProjectsPage


@pytest.mark.projects
@pytest.mark.regression
@pytest.mark.ui
class TestProjects:
    @allure.title("Test successful project creation")
    def test_successful_project_creation(self, projects_page: ProjectsPage):
        projects_page.check_title()
        projects_page.check_create_project_button()
        projects_page.click_create_project_button()
        projects_page.create_project_form.check_project_form()
        data = projects_page.create_project_form.fill_project_form()
        projects_page.create_project_form.check_project_form(data)
        projects_page.create_project_form.click_submit_button()
        projects_page.check_current_url("/projects")
        projects_page.check_projects_cards()


    @allure.title("Test successful project editing after creation")
    def test_successful_project_editing_after_creation(self, projects_page: ProjectsPage):
        projects_page.click_create_project_button()
        projects_page.create_project_form.check_project_form()
        data = projects_page.create_project_form.fill_project_form()
        projects_page.create_project_form.click_submit_button()
        project_card = projects_page.project_card_by_title(data)
        projects_page.check_current_url("/projects")
        project_card.click_edit_button()
        projects_page.edit_project_form.check_project_form(data)
        data = projects_page.edit_project_form.fill_project_form()
        projects_page.edit_project_form.check_project_form(data)
        projects_page.edit_project_form.click_submit_button()
        project_card = projects_page.project_card_by_title(data)
        projects_page.check_current_url("/projects")
        project_card.check_title(data['title'])
        project_card.check_description(data['description'])
