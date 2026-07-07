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
        login_page.check_register_text()
        login_page.check_register_link()
        login_page.login_form.check_login_button()
        login_page.login_form.click_login_button()
