from typing import Generator, List

import pytest
from pydantic import BaseModel

from api.clients.authentication.authentication_schema import AuthenticatedUserSchema
from api.clients.projects.projects_client import ProjectsClient
from api.clients.projects.projects_schema import ProjectSchema
from api.clients.tasks.tasks_client import get_tasks_client, TasksClient
from api.clients.tasks.tasks_schema import CreateTaskRequestSchema, CreateTaskResponseSchema, TaskSchema
from api.fixtures.projects import ProjectFixture
from api.fixtures.users import UserFixture
from tools.api.fakers import fake


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
def tasks_client_for_ui(function_auth_user: AuthenticatedUserSchema) -> TasksClient:
    return get_tasks_client(function_auth_user.authentication_user)


@pytest.fixture
def function_task(projects_client: ProjectsClient,
                  function_project: ProjectFixture) -> TaskFixture:
    request = CreateTaskRequestSchema()
    response = projects_client.create_project_task(function_project.id, request)

    return TaskFixture(request=request, response=response)


@pytest.fixture
def function_task_for_ui(projects_client: ProjectsClient,
                  function_project: ProjectFixture) -> TaskFixture:
    request = CreateTaskRequestSchema()
    response = projects_client.create_project_task(function_project.id, request)

    return TaskFixture(request=request, response=response)


@pytest.fixture
def created_tasks_for_project(
        created_project: ProjectSchema,
        projects_client_for_ui: ProjectsClient,
        tasks_client_for_ui: TasksClient
) -> Generator[List[TaskSchema], None, None]:
    tasks_data: List[TaskSchema] = []
    tasks_count = fake.integer(1, 5)

    for _ in range(tasks_count):
        create_task_request = CreateTaskRequestSchema()
        create_task_response = projects_client_for_ui.create_project_task(created_project.id,
                                                                         create_task_request)
        tasks_data.append(create_task_response.task)

    yield tasks_data

    for task in tasks_data:
        try:
            tasks_client_for_ui.delete_task_api(task.id)
        except Exception as e:
            pass


@pytest.fixture
def created_task_for_project(
        projects_client_for_ui: ProjectsClient,
        tasks_client_for_ui: TasksClient,
        created_project: ProjectSchema
) -> Generator[TaskSchema, None, None]:
    task_data: TaskSchema

    create_task_request = CreateTaskRequestSchema()
    create_task_response = projects_client_for_ui.create_project_task(created_project.id,
                                                                      create_task_request)

    task_data = create_task_response.task

    yield task_data

    try:
        tasks_client_for_ui.delete_task_api(task_data.id)
    except Exception as e:
        pass
