import allure
from httpx import Client, Response

from api.clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.api.routes import APIRoutes


class AttachmentsClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Get attachment by id {attachment_id}")
    def get_attachment_api(self, attachment_id: str) -> Response:
        return self.client.get(f"{APIRoutes.ATTACHMENTS}/{attachment_id}")

    @allure.step("Delete attachment by id {attachment_id}")
    def delete_attachment_api(self, attachment_id: str) -> Response:
        return self.client.delete(f"{APIRoutes.ATTACHMENTS}/{attachment_id}")


def get_attachments_client(authentication_user: AuthenticationUserSchema) -> AttachmentsClient:
    return AttachmentsClient(client=get_private_http_client(authentication_user))
