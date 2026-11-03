from typing import Generator, List

import pytest
from pydantic import BaseModel

from api.clients.attachments.attachments_client import AttachmentsClient, get_attachments_client
from api.clients.attachments.attachments_schema import AttachmentSchema, CreateAttachmentRequestSchema, \
    CreateAttachmentResponseSchema
from api.clients.authentication.authentication_schema import AuthenticatedUserSchema
from api.clients.tasks.tasks_client import TasksClient
from api.clients.tasks.tasks_schema import TaskSchema
from config import settings
from api.fixtures.tasks import TaskFixture
from api.fixtures.users import UserFixture
from tools.api.fakers import fake


class AttachmentFixture(BaseModel):
    request: CreateAttachmentRequestSchema
    response: CreateAttachmentResponseSchema

    @property
    def id(self):
        return self.response.attachment.id


@pytest.fixture
def attachments_client(function_user: UserFixture):
    return get_attachments_client(function_user.authentication_user)


@pytest.fixture
def attachments_client_for_ui(function_auth_user: AuthenticatedUserSchema) -> AttachmentsClient:
    return get_attachments_client(function_auth_user.authentication_user)


@pytest.fixture
def function_attachment(function_task: TaskFixture,
                        tasks_client: TasksClient) -> AttachmentFixture:
    request = CreateAttachmentRequestSchema(upload_file=settings.test_data.attachment_file)
    response = tasks_client.create_task_attachment(function_task.id, request)

    return AttachmentFixture(request=request, response=response)


@pytest.fixture
def created_attachments_for_task(
        created_task_for_project: TaskSchema,
        tasks_client_for_ui: TasksClient,
        attachments_client_for_ui: AttachmentsClient
) -> Generator[List[AttachmentSchema], None, None]:
    attachments_data: List[AttachmentSchema] = []
    attachments_count = fake.integer(1, 5)

    for _ in range(attachments_count):
        create_attachment_request = CreateAttachmentRequestSchema(
            upload_file=settings.test_data.attachment_file
        )
        create_attachment_response = tasks_client_for_ui.create_task_attachment(
            created_task_for_project.id,
            create_attachment_request
        )
        attachments_data.append(create_attachment_response.attachment)

    yield attachments_data

    for attachment in attachments_data:
        try:
            attachments_client_for_ui.delete_attachment_api(attachment.id)
        except Exception as e:
            pass
