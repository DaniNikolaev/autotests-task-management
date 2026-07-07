import pytest
from pydantic import BaseModel

from api.clients.attachments.attachments_client import get_attachments_client
from api.clients.attachments.attachments_schema import CreateAttachmentRequestSchema, CreateAttachmentResponseSchema
from api.clients.tasks.tasks_client import TasksClient
from config import settings
from api.fixtures.tasks import TaskFixture
from api.fixtures.users import UserFixture


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
def function_attachment(function_task: TaskFixture,
                        tasks_client: TasksClient) -> AttachmentFixture:
    request = CreateAttachmentRequestSchema(upload_file=settings.test_data.attachment_file)
    response = tasks_client.create_task_attachment(function_task.id, request)

    return AttachmentFixture(request=request, response=response)
