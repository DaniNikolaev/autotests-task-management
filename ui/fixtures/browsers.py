import json
from typing import List, Any, Generator

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from api.clients.authentication.authentication_client import AuthenticationClient
from api.clients.authentication.authentication_schema import LoginRequestSchema, TokenSchema, AuthenticatedUserSchema
from api.clients.projects.projects_client import ProjectsClient
from api.clients.projects.projects_schema import CreateProjectRequestSchema
from api.clients.users.public_users_client import PublicUsersClient
from api.clients.users.users_schema import CreateUserRequestSchema
from config import settings
from tools.api.fakers import fake
from tools.ui.playwright.pages import initialize_playwright_page
from tools.ui.routes import AppRoute
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage
from ui.pages.projects.projects_page import ProjectsPage


@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright,
                             session_auth_user: AuthenticatedUserSchema) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    context.add_init_script(f"""
        localStorage.setItem('accessToken', {json.dumps(session_auth_user.token.access_token)});
        localStorage.setItem('refreshToken', {json.dumps(session_auth_user.token.refresh_token)});
    """)
    page = context.new_page()
    page.goto("/login")
    context.storage_state(path=settings.browser_state_file)


@pytest.fixture(params=settings.browsers)
def browser_page_with_auth(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          storage_state=settings.browser_state_file,
                                          browser_type=request.param)
