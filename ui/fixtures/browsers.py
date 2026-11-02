import json

import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from api.clients.authentication.authentication_schema import AuthenticatedUserSchema
from config import settings
from tools.ui.playwright.pages import initialize_playwright_page


@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)


@pytest.fixture
def initialize_browser_state(playwright: Playwright,
                             function_auth_user: AuthenticatedUserSchema) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    try:
        context = browser.new_context(base_url=settings.get_base_url())
        context.add_init_script(f"""
            localStorage.setItem('accessToken', {json.dumps(function_auth_user.token.access_token)});
            localStorage.setItem('refreshToken', {json.dumps(function_auth_user.token.refresh_token)});
        """)
        page = context.new_page()
        page.goto("/login")
        context.storage_state(path=settings.browser_state_file)
    finally:
        browser.close()


@pytest.fixture(params=settings.browsers)
def browser_page_with_auth(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          storage_state=settings.browser_state_file,
                                          browser_type=request.param)



