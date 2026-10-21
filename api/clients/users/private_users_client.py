import allure
from httpx import Client, Response

from api.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from api.clients.users.users_schema import UpdateUserRequestSchema, GetUserResponseSchema
from tools.api.routes import APIRoutes


class PrivateUsersClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Get user me api")
    def get_user_me_api(self) -> Response:
        return self.client.get(f"{APIRoutes.USERS}/me")

    @allure.step("Get user me")
    def get_user_me(self) -> GetUserResponseSchema:
        response = self.get_user_me_api()
        return GetUserResponseSchema.model_validate_json(response.text)

    @allure.step("Get user by id {user_id}")
    def get_user_api(self, user_id: str) -> Response:
        return self.client.get(f"{APIRoutes.USERS}/{user_id}")

    @allure.step("Update user by id {user_id}")
    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        return self.client.patch(f"{APIRoutes.USERS}/{user_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete user by id {user_id}")
    def delete_user_api(self, user_id: str) -> Response:
        return self.client.delete(f"{APIRoutes.USERS}/{user_id}")


def get_private_users_client(authentication_user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(authentication_user))
