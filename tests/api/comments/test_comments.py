from http import HTTPStatus

import allure
import pytest

from api.clients.comments.comments_client import CommentsClient
from api.clients.comments.comments_schema import CreateCommentRequestSchema, CreateCommentResponseSchema, \
    GetCommentsResponseSchema, GetCommentResponseSchema, UpdateCommentRequestSchema, UpdateCommentResponseSchema
from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.tasks.tasks_client import TasksClient
from api.fixtures.comments import CommentFixture
from api.fixtures.tasks import TaskFixture
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.comments import assert_create_comment_response, assert_get_comments_response, \
    assert_get_comment_response, assert_update_comment_response, assert_comment_not_found_response
from tools.api.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.comments
class TestComments:
    @allure.title("Create comment")
    def test_create_comment(self,
                            tasks_client: TasksClient,
                            function_task: TaskFixture):
        request = CreateCommentRequestSchema()
        response = tasks_client.create_task_comment_api(function_task.id, request)
        response_data = CreateCommentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_comment_response(request, response_data)
        validate_json_schema(response.json(), CreateCommentResponseSchema.model_json_schema())

    @allure.title("Get comments")
    def test_get_comments(self,
                          tasks_client: TasksClient,
                          function_task: TaskFixture,
                          function_comment: CommentFixture):
        response = tasks_client.get_task_comments_api(function_task.id)
        response_data = GetCommentsResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_comments_response(response_data, [function_comment.response])
        validate_json_schema(response.json(), GetCommentsResponseSchema.model_json_schema())

    @allure.title("Get comment")
    def test_get_comment(self,
                         comments_client: CommentsClient,
                         function_comment: CommentFixture):
        response = comments_client.get_comment_api(function_comment.id)
        response_data = GetCommentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_comment_response(response_data, function_comment.response)
        validate_json_schema(response.json(), GetCommentResponseSchema.model_json_schema())

    @allure.title("Update comment")
    def test_update_comment(self,
                            comments_client: CommentsClient,
                            function_comment: CommentFixture):
        request = UpdateCommentRequestSchema()
        response = comments_client.update_comment_api(function_comment.id, request)
        response_data = UpdateCommentResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_comment_response(request, response_data)
        validate_json_schema(response.json(), UpdateCommentResponseSchema.model_json_schema())

    @allure.title("Delete comment")
    def test_delete_comment(self,
                            comments_client: CommentsClient,
                            function_comment: CommentFixture):
        delete_response = comments_client.delete_comment_api(function_comment.id)
        assert_status_code(delete_response.status_code, HTTPStatus.NO_CONTENT)

        get_response = comments_client.get_comment_api(function_comment.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_comment_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())
