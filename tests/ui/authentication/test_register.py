import allure
import pytest

from tools.api.fakers import fake
from ui.pages.authentication.registration_page import RegistrationPage


@pytest.mark.authentication
@pytest.mark.register
@pytest.mark.regression
@pytest.mark.ui
class TestRegister:
    @allure.title("Test successful registration")
    def test_successful_registration(self,
                                     registration_page: RegistrationPage,
                                     #projects_page: ProjectsPage,
                                     ):
        data = fake.registration_form()
        registration_page.check_title()
        registration_page.registration_form.check_form()
        registration_page.registration_form.fill_form(data)
        registration_page.registration_form.check_form(data)
        registration_page.registration_form.check_registration_button()
        registration_page.check_login_text()
        registration_page.check_login_link()
        registration_page.registration_form.click_registration_button()
