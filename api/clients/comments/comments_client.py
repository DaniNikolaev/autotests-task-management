import allure
from httpx import Client, Response

from api.clients.comments.comments_schema import UpdateCommentRequestSchema
from api.clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from tools.api.routes import APIRoutes


class CommentsClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Get comment by id {comment_id}")
    def get_comment_api(self, comment_id: str) -> Response:
        return self.client.get(f"{APIRoutes.COMMENTS}/{comment_id}")

    @allure.step("Update comment by id {comment_id}")
    def update_comment_api(self, comment_id: str, request: UpdateCommentRequestSchema) -> Response:
        return self.client.patch(f"{APIRoutes.COMMENTS}/{comment_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete comment by id {comment_id}")
    def delete_comment_api(self, comment_id: str) -> Response:
        return self.client.delete(f"{APIRoutes.COMMENTS}/{comment_id}")


def get_comments_client(authentication_user: AuthenticationUserSchema) -> CommentsClient:
    return CommentsClient(client=get_private_http_client(authentication_user))
