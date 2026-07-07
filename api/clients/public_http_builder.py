from httpx import Client

from config import settings


def get_public_http_client() -> Client:
    return Client(
        timeout=settings.http_client.timeout,
        base_url=settings.http_client.client_url,
    )
