import allure
from httpx import Client, Response

from api.clients.attachments.attachments_schema import CreateAttachmentRequestSchema, CreateAttachmentResponseSchema
from api.clients.comments.comments_schema import CreateCommentRequestSchema, CreateCommentResponseSchema
from api.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from api.clients.tasks.tasks_schema import UpdateTaskRequestSchema
from tools.api.routes import APIRoutes


class TasksClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Get task by id {task_id}")
    def get_task_api(self, task_id: str) -> Response:
        return self.client.get(f"{APIRoutes.TASKS}/{task_id}")

    @allure.step("Update task by id {task_id}")
    def update_task_api(self, task_id: str, request: UpdateTaskRequestSchema) -> Response:
        return self.client.patch(f"{APIRoutes.TASKS}/{task_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete tasks by id {task_id}")
    def delete_task_api(self, task_id: str) -> Response:
        return self.client.delete(f"{APIRoutes.TASKS}/{task_id}")

    @allure.step("Create task attachment")
    def create_task_attachment_api(self, task_id: str, request: CreateAttachmentRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.TASKS}/{task_id}/attachments",
                                data=request.model_dump(by_alias=True, exclude={"upload_file"}),
                                files={"upload_file": request.upload_file.read_bytes()})

    def create_task_attachment(self, task_id: str, request: CreateAttachmentRequestSchema) -> Response:
        response = self.create_task_attachment_api(task_id, request)
        return CreateAttachmentResponseSchema.model_validate_json(response.text)

    @allure.step("Create task comment")
    def create_task_comment_api(self, task_id: str, request: CreateCommentRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.TASKS}/{task_id}/comments", json=request.model_dump(by_alias=True))

    def create_task_comment(self, task_id: str, request: CreateCommentRequestSchema) -> Response:
        response = self.create_task_comment_api(task_id, request)
        return CreateCommentResponseSchema.model_validate_json(response.text)

    @allure.step("Get task comments")
    def get_task_comments_api(self, task_id: str):
        return self.client.get(f"{APIRoutes.TASKS}/{task_id}/comments")


def get_tasks_client(authentication_user: AuthenticationUserSchema) -> TasksClient:
    return TasksClient(client=get_private_http_client(authentication_user))
