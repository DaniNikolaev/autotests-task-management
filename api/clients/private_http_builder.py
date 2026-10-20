from functools import lru_cache

from httpx import Client
from pydantic import BaseModel

from api.clients.authentication.authentication_client import get_authentication_client
from api.clients.authentication.authentication_schema import LoginRequestSchema, AuthenticationUserSchema
from config import settings





@lru_cache(maxsize=None)
def get_private_http_client(user: AuthenticationUserSchema) -> Client:
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email, password=user.password)
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
        headers={"Authorization": f"Bearer {login_response.token.access_token}"}
    )
