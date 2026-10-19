import allure
import pytest

from api.fixtures.users import UserFixture
from tools.api.fakers import fake
from ui.pages.authentication.login_page import LoginPage
from ui.pages.authentication.registration_page import RegistrationPage


@pytest.mark.authentication
@pytest.mark.register
@pytest.mark.regression
@pytest.mark.ui
class TestRegister:
    @allure.title("Test successful registration")
    def test_successful_registration(self,
                                     login_page: LoginPage,
                                     registration_page: RegistrationPage
                                     ):
        data = fake.registration_form()
        registration_page.check_title()
        registration_page.registration_form.check_form()
        registration_page.registration_form.fill_form(data)
        registration_page.registration_form.check_form(data)
        registration_page.registration_form.check_registration_button()
        registration_page.check_login_link()
        registration_page.registration_form.click_registration_button()
        login_page.check_current_url("/login")
        login_page.login_form.fill_form(data)
        login_page.login_form.click_login_button()
        login_page.check_current_url("/projects")

    @allure.title("Test incorrect credits")
    @pytest.mark.parametrize("data", (
        {"email": "email", "password": "password", "first_name": "first_name", "last_name": "last_name"},
        {"email": "", "password": "password", "first_name": "first_name", "last_name": "last_name"},
        {"email": "email", "password": "", "first_name": "first_name", "last_name": "last_name"},
        {"email": "email", "password": "password", "first_name": "", "last_name": "last_name"},
        {"email": "email", "password": "password", "first_name": "first_name", "last_name": ""},
        {"email": "", "password": "", "first_name": "", "last_name": ""},
        {"email": "email@email.com", "password": "pass", "first_name": "first_name", "last_name": "last_name"}
    ))
    def test_incorrect_credits_registration(self, registration_page: RegistrationPage, data: dict):
        registration_page.registration_form.fill_form(data)
        registration_page.registration_form.check_form(data)
        registration_page.registration_form.click_registration_button()
        registration_page.check_current_url("/register")

    @allure.title("Test registration with existing email")
    def test_registration_with_existing_email(self, registration_page: RegistrationPage, function_user: UserFixture):
        data = fake.registration_form()
        data['email'] = function_user.email
        registration_page.registration_form.fill_form(data)
        registration_page.registration_form.check_form(data)
        registration_page.registration_form.click_registration_button()
        registration_page.registration_form.check_error_message(function_user.email)
        registration_page.check_current_url("/register")

    @allure.title("Test navigate to login")
    def test_navigate_to_login(self, registration_page: RegistrationPage):
        registration_page.check_login_link()
        registration_page.check_current_url("/register")
        registration_page.login_link.click()
        registration_page.check_current_url("/login")