import allure
import pytest

from api.fixtures.users import UserFixture
from ui.pages.authentication.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.authentication
@pytest.mark.login
class TestLogin:
    @allure.title("Test successful login")
    def test_successful_login(self, function_user: UserFixture, login_page: LoginPage):
        data = {"email": function_user.email, "password": function_user.password}
        login_page.check_title()
        login_page.login_form.check_form()
        login_page.login_form.fill_form(data)
        login_page.login_form.check_form(data)
        login_page.check_register_link()
        login_page.login_form.check_login_button()
        login_page.login_form.click_login_button()
        login_page.check_current_url("/projects")

    @allure.title("Test incorrect login or password")
    @pytest.mark.parametrize("data", (
        {"email": "email", "password": "password"},
        {"email": "", "password": "password"},
        {"email": "email", "password": ""},
        {"email": "", "password": ""},
    ))
    def test_incorrect_login_or_password(self, login_page: LoginPage, data: dict):
        login_page.login_form.fill_form(data)
        login_page.login_form.check_form(data)
        login_page.login_form.click_login_button()
        login_page.check_current_url("/login")

    @allure.title("Test failed login")
    @pytest.mark.parametrize("data", (
        {"email": "email@email.com", "password": "password"},
        {"email": "111@111.com", "password": "111"},
        {"email": ".@com", "password": "////"}
    ))
    def test_failed_login(self, login_page: LoginPage, data: dict):
        login_page.login_form.fill_form(data)
        login_page.login_form.check_form(data)
        login_page.login_form.click_login_button()
        login_page.check_current_url("/login")
        login_page.login_form.check_error_message()

    @allure.title("Test navigate to register")
    def test_navigate_to_register(self, login_page: LoginPage):
        login_page.check_register_link()
        login_page.check_current_url("/login")
        login_page.register_link.click()
        login_page.check_current_url("/register")