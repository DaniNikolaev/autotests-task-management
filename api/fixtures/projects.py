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


@pytest.fixture(scope="session")
def session_projects_client(session_auth_user: AuthenticatedUserSchema) -> ProjectsClient:
    return get_projects_client(session_auth_user.authentication_user)


@pytest.fixture
def function_project(projects_client: ProjectsClient) -> ProjectFixture:
    request = CreateProjectRequestSchema()
    response = projects_client.create_project(request)

    return ProjectFixture(request=request, response=response)


@pytest.fixture
def created_projects(
        session_projects_client: ProjectsClient
) -> Generator[List[ProjectSchema], None, None]:
    projects_data: List[ProjectSchema] = []
    projects_count = fake.integer(1, 5)

    for _ in range(projects_count):
        create_project_request = CreateProjectRequestSchema()
        create_project_response = session_projects_client.create_project(create_project_request)

        projects_data.append(create_project_response.project)

    yield projects_data
    for project in projects_data:
        #try:
            response = session_projects_client.delete_project_api(project.id)
        #except Exception as e:
           # pass
