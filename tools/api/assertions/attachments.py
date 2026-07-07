import allure

from api.clients.attachments.attachments_schema import AttachmentSchema, CreateAttachmentRequestSchema, \
    CreateAttachmentResponseSchema, GetAttachmentResponseSchema
from api.clients.errors_schema import InternalErrorResponseSchema
from tools.api.assertions.base import assert_equal
from tools.api.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("ATTACHMENTS_ASSERTIONS")


@allure.step("Check attachment")
def assert_attachment(actual: AttachmentSchema, expected: AttachmentSchema):
    logger.info("Check attachment")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.filename, expected.filename, "filename")
    assert_equal(actual.directory, expected.directory, "directory")
    assert_equal(actual.task_id, expected.task_id, "task_id")
    assert_equal(actual.uploaded_by, expected.uploaded_by, "uploaded_by")
    assert_equal(actual.created_at, expected.created_at, "created_at")
    assert_equal(actual.url, expected.url, "url")


@allure.step("Check create attachment response")
def assert_create_attachment_response(request: CreateAttachmentRequestSchema,
                                      response: CreateAttachmentResponseSchema):
    logger.info("Check create attachment response")
    assert_equal(request.filename, response.attachment.filename, "filename")
    assert_equal(request.directory, response.attachment.directory, "directory")


@allure.step("Check get attachment response")
def assert_get_attachment_response(get_attachment_response: GetAttachmentResponseSchema,
                                   create_attachment_response: CreateAttachmentResponseSchema):
    logger.info("Check get attachment response")
    assert_attachment(get_attachment_response.attachment, create_attachment_response.attachment)


@allure.step("Check attachment not found response")
def assert_attachment_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(
        details="Attachment not found"
    )
    logger.info("Check attachment not found response")
    assert_internal_error_response(actual, expected)
