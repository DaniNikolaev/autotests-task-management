from http import HTTPStatus

import allure
import pytest

from api.clients.authentication.authentication_client import AuthenticationClient
from api.clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from api.fixtures.users import UserFixture
from tools.api.assertions.authentication import assert_login_response
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.authentication
class TestAuthentication:
    @allure.title("Success login")
    def test_login(self,
                   function_user: UserFixture,
                   authentication_client: AuthenticationClient):
        request = LoginRequestSchema(
            email=function_user.email,
            password=function_user.password
        )
        response = authentication_client.login_api(request)
        response_data = LoginResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)
        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())
