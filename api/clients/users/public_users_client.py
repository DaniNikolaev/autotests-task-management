import allure
from httpx import Client, Response

from api.clients.public_http_builder import get_public_http_client
from api.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.api.routes import APIRoutes


class PublicUsersClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.client.post(APIRoutes.USERS, json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())
