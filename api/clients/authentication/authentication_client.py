import allure
from httpx import Client, Response

from api.clients.authentication.authentication_schema import LoginRequestSchema, RefreshRequestSchema, LogoutRequestSchema, \
    LoginResponseSchema
from api.clients.public_http_builder import get_public_http_client
from tools.api.routes import APIRoutes


class AuthenticationClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Authenticate user")
    def login_api(self, request: LoginRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.AUTHENTICATION}/login", json=request.model_dump(by_alias=True))

    def login(self, request: LoginRequestSchema) -> LoginResponseSchema:
        response = self.login_api(request)
        return LoginResponseSchema.model_validate_json(response.text)

    @allure.step("Refresh user token")
    def refresh_api(self, request: RefreshRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.AUTHENTICATION}/refresh", json=request.model_dump(by_alias=True))

    @allure.step("Logout user")
    def logout_api(self, request: LogoutRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.AUTHENTICATION}/logout", json=request.model_dump(by_alias=True))


def get_authentication_client() -> AuthenticationClient:
    return AuthenticationClient(client=get_public_http_client())
