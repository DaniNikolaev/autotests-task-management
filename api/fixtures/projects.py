import pytest
from pydantic import BaseModel

from api.clients.projects.projects_client import ProjectsClient, get_projects_client
from api.clients.projects.projects_schema import CreateProjectRequestSchema, CreateProjectResponseSchema
from api.fixtures.users import UserFixture


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
def function_project(projects_client: ProjectsClient) -> ProjectFixture:
    request = CreateProjectRequestSchema()
    response = projects_client.create_project(request)

    return ProjectFixture(request=request, response=response)
