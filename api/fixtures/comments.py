from typing import Generator, List

import pytest
from pydantic import BaseModel

from api.clients.authentication.authentication_schema import AuthenticatedUserSchema
from api.clients.comments.comments_client import CommentsClient, get_comments_client
from api.clients.comments.comments_schema import CreateCommentRequestSchema, CreateCommentResponseSchema, CommentSchema
from api.clients.tasks.tasks_client import TasksClient
from api.clients.tasks.tasks_schema import TaskSchema
from api.fixtures.tasks import TaskFixture
from api.fixtures.users import UserFixture
from tools.api.fakers import fake


class CommentFixture(BaseModel):
    request: CreateCommentRequestSchema
    response: CreateCommentResponseSchema

    @property
    def id(self):
        return self.response.comment.id


@pytest.fixture
def comments_client(function_user: UserFixture) -> CommentsClient:
    return get_comments_client(function_user.authentication_user)


@pytest.fixture
def comments_client_for_ui(function_auth_user: AuthenticatedUserSchema) -> CommentsClient:
    return get_comments_client(function_auth_user.authentication_user)


@pytest.fixture
def function_comment(comments_client: CommentsClient,
                     tasks_client: TasksClient,
                     function_task: TaskFixture):
    request = CreateCommentRequestSchema()
    response = tasks_client.create_task_comment(function_task.id, request)

    return CommentFixture(request=request, response=response)


@pytest.fixture
def created_comments_for_tasks(
        created_task_for_project: TaskSchema,
        tasks_client_for_ui: TasksClient,
        comments_client_for_ui: CommentsClient
) -> Generator[List[CommentSchema], None, None]:
    comments_data: List[CommentSchema] = []
    comments_count = fake.integer(1, 5)

    for _ in range(comments_count):
        create_comment_request = CreateCommentRequestSchema()
        create_comment_response = tasks_client_for_ui.create_task_comment(
            created_task_for_project.id,
            create_comment_request
        )
        comments_data.append(create_comment_response.comment)

    yield comments_data

    for comment in comments_data:
        try:
            comments_client_for_ui.delete_comment_api(comment.id)
        except Exception as e:
            pass
