from typing import List, Generator

import pytest
from pydantic import BaseModel

from api.clients.authentication.authentication_schema import AuthenticatedUserSchema
from api.clients.projects.projects_client import ProjectsClient, get_projects_client
from api.clients.projects.projects_schema import CreateProjectRequestSchema, CreateProjectResponseSchema, ProjectSchema
from api.fixtures.users import UserFixture
from tools.api.fakers import Fake, fake


class ProjectFixture(BaseModel):
    request: CreateProjectRequestSchema
    response: CreateProjectResponseSchema

    @property
    def id(self):
        return self.response.project.id


@pytest.fixture
def projects_client(function_user: UserFixture) -> ProjectsClient:
    return get_projects_client(function_user.authentication_user)


@pytest.fixture
def projects_client_for_ui(function_auth_user: AuthenticatedUserSchema) -> ProjectsClient:
    return get_projects_client(function_auth_user.authentication_user)


@pytest.fixture
def function_project(projects_client: ProjectsClient) -> ProjectFixture:
    request = CreateProjectRequestSchema()
    response = projects_client.create_project(request)

    return ProjectFixture(request=request, response=response)


@pytest.fixture
def function_project_for_ui(projects_client_for_ui: ProjectsClient) -> ProjectFixture:
    request = CreateProjectRequestSchema()
    response = projects_client_for_ui.create_project(request)

    return ProjectFixture(request=request, response=response)


@pytest.fixture
def created_projects(
        projects_client_for_ui: ProjectsClient
) -> Generator[List[ProjectSchema], None, None]:
    projects_data: List[ProjectSchema] = []
    projects_count = fake.integer(1, 5)

    for _ in range(projects_count):
        create_project_request = CreateProjectRequestSchema()
        create_project_response = projects_client_for_ui.create_project(create_project_request)

        projects_data.append(create_project_response.project)

    yield projects_data
    for project in projects_data:
        try:
            projects_client_for_ui.delete_project_api(project.id)
        except Exception as e:
            pass


@pytest.fixture
def created_project(
        projects_client_for_ui: ProjectsClient
) -> Generator[ProjectSchema, None, None]:
    project_data: ProjectSchema

    create_project_request = CreateProjectRequestSchema()
    create_project_response = projects_client_for_ui.create_project(create_project_request)

    project_data = create_project_response.project

    yield project_data

    try:
        projects_client_for_ui.delete_project_api(project_data.id)
    except Exception as e:
        pass
