import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Playwright, Page

from config import settings
from tools.ui.playwright.pages import initialize_playwright_page
from tools.ui.routes import AppRoute
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage


@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright, test_name=request.node.name, browser_type=request.param)


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit(AppRoute.REGISTRATION)

    data = {"email": settings.test_user.email,
            "password": settings.test_user.password,
            "first_name": settings.test_user.first_name,
            "last_name": settings.test_user.last_name}
    registration_page.registration_form.fill_form(data)
    registration_page.registration_form.click_registration_button()
    login_page = LoginPage(page)
    login_page.login_form.fill_form(data)
    login_page.login_form.click_login_button()
    page.wait_for_url("**/projects")
    context.storage_state(path=settings.browser_state_file)


@pytest.fixture(params=settings.browsers)
def browser_page_with_state(initialize_browser_state, request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          storage_state=settings.browser_state_file,
                                          browser_type=request.param)
