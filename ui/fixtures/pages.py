import pytest
from playwright.sync_api import Page

from tools.ui.routes import AppRoute
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage


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
