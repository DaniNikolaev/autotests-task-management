from http import HTTPStatus

import allure
import pytest

from api.clients.attachments.attachments_client import AttachmentsClient
from api.clients.attachments.attachments_schema import CreateAttachmentRequestSchema, CreateAttachmentResponseSchema, \
    GetAttachmentResponseSchema
from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.tasks.tasks_client import TasksClient
from config import settings
from api.fixtures.attachments import AttachmentFixture
from api.fixtures.tasks import TaskFixture
from tools.api.assertions.attachments import assert_create_attachment_response, assert_get_attachment_response, \
    assert_attachment_not_found_response
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.attachments
class TestAttachments:
    @allure.title("Create attachment")
    def test_create_attachment(self,
                               tasks_client: TasksClient,
                               function_task: TaskFixture):
        request = CreateAttachmentRequestSchema(upload_file=settings.test_data.attachment_file)
        response = tasks_client.create_task_attachment_api(function_task.id, request)
        response_data = CreateAttachmentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_attachment_response(request, response_data)
        validate_json_schema(response.json(), CreateAttachmentResponseSchema.model_json_schema())

    @allure.title("Get attachment")
    def test_get_attachment(self,
                            attachments_client: AttachmentsClient,
                            function_attachment: AttachmentFixture):
        response = attachments_client.get_attachment_api(function_attachment.id)
        response_data = GetAttachmentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_attachment_response(response_data, function_attachment.response)
        validate_json_schema(response.json(), GetAttachmentResponseSchema.model_json_schema())

    @allure.title("Delete attachment")
    def test_delete_attachment(self,
                               attachments_client: AttachmentsClient,
                               function_attachment: AttachmentFixture):
        delete_response = attachments_client.delete_attachment_api(function_attachment.id)
        assert_status_code(delete_response.status_code, HTTPStatus.NO_CONTENT)

        get_response = attachments_client.get_attachment_api(function_attachment.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_attachment_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())
