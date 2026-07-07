import pytest
from pydantic import BaseModel

from api.clients.projects.projects_client import ProjectsClient
from api.clients.tasks.tasks_client import get_tasks_client
from api.clients.tasks.tasks_schema import CreateTaskRequestSchema, CreateTaskResponseSchema
from api.fixtures.projects import ProjectFixture
from api.fixtures.users import UserFixture


class TaskFixture(BaseModel):
    request: CreateTaskRequestSchema
    response: CreateTaskResponseSchema

    @property
    def id(self):
        return self.response.task.id


@pytest.fixture
def tasks_client(function_user: UserFixture):
    return get_tasks_client(function_user.authentication_user)


@pytest.fixture
def function_task(projects_client: ProjectsClient,
                  function_project: ProjectFixture) -> TaskFixture:
    request = CreateTaskRequestSchema()
    response = projects_client.create_project_task(function_project.id, request)

    return TaskFixture(request=request, response=response)
