from typing import Generator, Any, List

import pytest
from playwright.sync_api import Page

from api.clients.projects.projects_client import ProjectsClient
from api.clients.projects.projects_schema import CreateProjectRequestSchema, ProjectSchema
from tools.api.fakers import fake
from tools.ui.routes import AppRoute
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage
from ui.pages.projects.project_page import ProjectPage
from ui.pages.projects.projects_page import ProjectsPage


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
