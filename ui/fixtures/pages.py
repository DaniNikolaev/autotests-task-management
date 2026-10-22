from typing import Generator, Any, List

import pytest
from playwright.sync_api import Page

from api.clients.comments.comments_schema import CommentSchema
from api.clients.projects.projects_client import ProjectsClient
from api.clients.projects.projects_schema import CreateProjectRequestSchema, ProjectSchema
from api.clients.tasks.tasks_client import TasksClient
from api.clients.tasks.tasks_schema import TaskSchema, CreateTaskRequestSchema
from api.fixtures.tasks import TaskFixture
from tools.api.fakers import fake
from tools.ui.routes import AppRoute
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage
from ui.pages.projects.project_page import ProjectPage
from ui.pages.projects.projects_page import ProjectsPage
from ui.pages.tasks.task_page import TaskPage


@pytest.fixture
def registration_page(browser_page: Page) -> RegistrationPage:
    p = RegistrationPage(page=browser_page)
    p.visit(AppRoute.REGISTRATION)
    return p


@pytest.fixture
def login_page(browser_page: Page) -> LoginPage:
    p = LoginPage(page=browser_page)
    p.visit(AppRoute.LOGIN)
    return p


@pytest.fixture
def projects_page(browser_page: Page) -> ProjectsPage:
    p = ProjectsPage(page=browser_page)
    p.visit(AppRoute.PROJECTS)
    return p


@pytest.fixture
def projects_page_with_auth(browser_page_with_auth: Page) -> ProjectsPage:
    p = ProjectsPage(page=browser_page_with_auth)
    p.visit(AppRoute.PROJECTS)
    return p


@pytest.fixture
def projects_page_with_data(
        browser_page_with_auth: Page,
        created_projects: List[ProjectSchema]
) -> Generator[ProjectsPage, Any, None]:
    projects_page = ProjectsPage(page=browser_page_with_auth)
    projects_page.visit(AppRoute.PROJECTS)

    yield projects_page


@pytest.fixture
def project_page(browser_page: Page) -> ProjectPage:
    p = ProjectPage(page=browser_page)
    p.visit(AppRoute.PROJECTS)
    return p


@pytest.fixture
def project_page_with_auth(
        browser_page_with_auth: Page,
        created_project: ProjectSchema
) -> Generator[ProjectPage, Any, None]:
    project_page = ProjectPage(page=browser_page_with_auth)
    project_page.visit(f"{AppRoute.PROJECTS}/{created_project.id}")

    yield project_page


@pytest.fixture
def project_page_with_tasks(
    browser_page_with_auth: Page,
    created_project: ProjectSchema,
    created_tasks_for_project: List[TaskSchema]
) -> Generator[ProjectPage, Any, None]:
    project_page = ProjectPage(page=browser_page_with_auth)
    project_page.visit(f"{AppRoute.PROJECTS.value}/{created_project.id}")

    yield project_page


@pytest.fixture
def task_page(browser_page: Page,
              created_project: ProjectSchema,
              function_task_for_ui: TaskFixture) -> ProjectPage:
    p = ProjectPage(page=browser_page)
    p.visit(f"{AppRoute.TASKS}{function_task_for_ui.id}")
    return p


@pytest.fixture
def task_page_with_auth(
        browser_page_with_auth: Page,
        created_project: ProjectSchema,
        created_task_for_project: TaskSchema
) -> Generator[TaskPage, Any, None]:
    task_page = TaskPage(page=browser_page_with_auth)
    task_page.visit(f"{AppRoute.TASKS}/{created_task_for_project.id}")

    yield task_page


@pytest.fixture
def task_page_with_comments(
    browser_page_with_auth: Page,
    created_task_for_project: TaskSchema,
    created_comments_for_tasks: List[CommentSchema]
) -> Generator[TaskPage, Any, None]:
    task_page = TaskPage(page=browser_page_with_auth)
    task_page.visit(f"/tasks/{created_task_for_project.id}")

    yield task_page
