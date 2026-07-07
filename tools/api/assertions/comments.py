import allure

from api.clients.comments.comments_schema import CommentSchema, CreateCommentRequestSchema, CreateCommentResponseSchema, \
    GetCommentResponseSchema, UpdateCommentRequestSchema, UpdateCommentResponseSchema, GetCommentsResponseSchema
from api.clients.errors_schema import InternalErrorResponseSchema
from tools.api.assertions.base import assert_equal, assert_length
from tools.api.assertions.errors import assert_internal_error_response
from tools.logger import get_logger


logger = get_logger("COMMENTS_ASSERTIONS")


@allure.step("Check comment")
def assert_comment(actual: CommentSchema, expected: CommentSchema):
    logger.info("Check comment")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.content, expected.content, "content")
    assert_equal(actual.is_edited, expected.is_edited, "is_edited")
    assert_equal(actual.related_task_id, expected.related_task_id, "related_task_id")
    assert_equal(actual.author_user_id, expected.author_user_id, "author_user_id")
    assert_equal(actual.created_at, expected.created_at, "created_at")
    assert_equal(actual.updated_at, expected.updated_at, "updated_at")


@allure.step("Check create comment response")
def assert_create_comment_response(request: CreateCommentRequestSchema,
                                   response: CreateCommentResponseSchema):
    logger.info("Check create comment response")
    assert_equal(request.content, response.comment.content, "content")


@allure.step("Check update comment response")
def assert_update_comment_response(request: UpdateCommentRequestSchema,
                                   response: UpdateCommentResponseSchema):
    logger.info("Check update comment response")
    assert_equal(request.content, response.comment.content, "content")


@allure.step("Check get comment response")
def assert_get_comment_response(get_comment_response: GetCommentResponseSchema,
                                create_comment_response: CreateCommentResponseSchema):
    logger.info("Check get comment response")
    assert_comment(get_comment_response.comment, create_comment_response.comment)


@allure.step("Check get comments response")
def assert_get_comments_response(get_comments_response: GetCommentsResponseSchema,
                                 create_comment_responses: list[CreateCommentResponseSchema]):
    assert_length(get_comments_response.comments, create_comment_responses, "comments")

    logger.info("Check get comments response")
    for i, create_comment_response in enumerate(create_comment_responses):
        assert_equal(get_comments_response.comments[i].id,
                     create_comment_response.comment.id, "id")
        assert_equal(get_comments_response.comments[i].content,
                     create_comment_response.comment.content, "content")
        assert_equal(get_comments_response.comments[i].is_edited,
                     create_comment_response.comment.is_edited, "is_edited")
        assert_equal(get_comments_response.comments[i].related_task_id,
                     create_comment_response.comment.related_task_id, "related_task_id")
        assert_equal(get_comments_response.comments[i].author_user_id,
                     create_comment_response.comment.author_user_id, "author_user_id")
        assert_equal(get_comments_response.comments[i].created_at,
                     create_comment_response.comment.created_at, "created_at")
        assert_equal(get_comments_response.comments[i].updated_at,
                     create_comment_response.comment.updated_at, "updated_at")


@allure.step("Check comment not found response")
def assert_comment_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(
        details="Comment not found"
    )
    logger.info("Check comment not found response")
    assert_internal_error_response(actual, expected)
