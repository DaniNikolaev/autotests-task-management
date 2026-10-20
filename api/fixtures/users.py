import pytest
from pydantic import BaseModel

from api.clients.authentication.authentication_client import AuthenticationClient
from api.clients.authentication.authentication_schema import LoginRequestSchema, TokenSchema, AuthenticatedUserSchema
from api.clients.private_http_builder import AuthenticationUserSchema
from api.clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from api.clients.users.public_users_client import PublicUsersClient, get_public_users_client
from api.clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema


class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def id(self):
        return self.response.user.id

    @property
    def email(self):
        return self.request.email

    @property
    def password(self):
        return self.request.password

    @property
    def authentication_user(self) -> AuthenticationUserSchema:
        return AuthenticationUserSchema(
            email=self.email,
            password=self.password
        )


@pytest.fixture
def public_users_client() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture(scope="session")
def public_users_client_session() -> PublicUsersClient:
    return get_public_users_client()


@pytest.fixture()
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response)


@pytest.fixture
def private_users_client(function_user: UserFixture) -> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)


@pytest.fixture(scope="session")
def session_auth_user(
        public_users_client_session: PublicUsersClient,
        authentication_client_session: AuthenticationClient
) -> AuthenticatedUserSchema:
    create_user_request = CreateUserRequestSchema()
    public_users_client_session.create_user(create_user_request)

    login_request = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = authentication_client_session.login(login_request)
    return AuthenticatedUserSchema(
        authentication_user=AuthenticationUserSchema(
            email=create_user_request.email,
            password=create_user_request.password
        ),
        token=login_response.token
    )
