import pytest
from pydantic import BaseModel

from api.clients.comments.comments_client import CommentsClient, get_comments_client
from api.clients.comments.comments_schema import CreateCommentRequestSchema, CreateCommentResponseSchema
from api.clients.tasks.tasks_client import TasksClient
from api.fixtures.tasks import TaskFixture
from api.fixtures.users import UserFixture


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
def function_comment(comments_client: CommentsClient,
                     tasks_client: TasksClient,
                     function_task: TaskFixture):
    request = CreateCommentRequestSchema()
    response = tasks_client.create_task_comment(function_task.id, request)

    return CommentFixture(request=request, response=response)
