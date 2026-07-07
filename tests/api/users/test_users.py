from http import HTTPStatus

import allure
import pytest

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.users.private_users_client import PrivateUsersClient
from api.clients.users.public_users_client import PublicUsersClient
from api.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema, \
    UpdateUserRequestSchema, UpdateUserResponseSchema
from api.fixtures.users import UserFixture
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.schema import validate_json_schema
from tools.api.assertions.users import assert_create_user_response, assert_get_user_response, \
    assert_update_user_response, assert_user_not_found_response


@pytest.mark.regression
@pytest.mark.users
class TestUsers:
    @allure.title("Create user")
    def test_create_user(self, public_users_client: PublicUsersClient):
        request = CreateUserRequestSchema()
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_user_response(request, response_data)
        validate_json_schema(response.json(), CreateUserResponseSchema.model_json_schema())

    @allure.title("Get user me")
    def test_get_user_me(self,
                         private_users_client: PrivateUsersClient,
                         function_user: UserFixture):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(function_user.request, response_data)
        validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())

    @allure.title("Get user")
    def test_get_user(self,
                      private_users_client: PrivateUsersClient,
                      function_user: UserFixture):
        response = private_users_client.get_user_api(function_user.id)
        response_data = GetUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(function_user.request, response_data)
        validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())

    @allure.title("Update user")
    def test_update_user(self,
                         private_users_client: PrivateUsersClient,
                         function_user: UserFixture):
        request = UpdateUserRequestSchema()
        response = private_users_client.update_user_api(request=request, user_id=function_user.id)
        response_data = UpdateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_user_response(request, response_data)
        validate_json_schema(response.json(), UpdateUserResponseSchema.model_json_schema())

    @allure.title("Delete user")
    def test_delete_user(self,
                         private_users_client: PrivateUsersClient,
                         public_users_client: PublicUsersClient,
                         function_user: UserFixture):
        create_request = CreateUserRequestSchema()
        create_response = public_users_client.create_user_api(create_request)
        create_response_data = CreateUserResponseSchema.model_validate_json(create_response.text)
        assert_status_code(create_response.status_code, HTTPStatus.CREATED)

        delete_response = private_users_client.delete_user_api(user_id=create_response_data.user.id)
        assert_status_code(delete_response.status_code, HTTPStatus.NO_CONTENT)

        get_response = private_users_client.get_user_api(user_id=create_response_data.user.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_user_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())
