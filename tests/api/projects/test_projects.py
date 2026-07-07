from http import HTTPStatus

import allure
import pytest

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.projects.projects_client import ProjectsClient
from api.clients.projects.projects_schema import CreateProjectRequestSchema, CreateProjectResponseSchema, \
    GetProjectsResponseSchema, GetProjectResponseSchema, UpdateProjectRequestSchema, UpdateProjectResponseSchema
from api.fixtures.projects import ProjectFixture
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.projects import assert_create_project_response, assert_get_projects_response, \
    assert_get_project_response, assert_update_project_response, assert_project_not_found_response
from tools.api.assertions.schema import validate_json_schema


@pytest.mark.regression
@pytest.mark.projects
class TestProjects:
    @allure.title("Create project")
    def test_create_project(self, projects_client: ProjectsClient):
        request = CreateProjectRequestSchema()
        response = projects_client.create_project_api(request)
        response_data = CreateProjectResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_project_response(request, response_data)
        validate_json_schema(response.json(), CreateProjectResponseSchema.model_json_schema())

    @allure.title("Get projects")
    def test_get_projects(self,
                          projects_client: ProjectsClient,
                          function_project: ProjectFixture):
        response = projects_client.get_projects_api()
        response_data = GetProjectsResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_projects_response(response_data, [function_project.response])
        validate_json_schema(response.json(), GetProjectsResponseSchema.model_json_schema())

    @allure.title("Get project")
    def test_get_project(self,
                         projects_client: ProjectsClient,
                         function_project: ProjectFixture):
        response = projects_client.get_project_api(function_project.id)
        response_data = GetProjectResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_project_response(response_data, function_project.response)
        validate_json_schema(response.json(), GetProjectResponseSchema.model_json_schema())

    @allure.title("Update project")
    def test_update_project(self,
                            projects_client: ProjectsClient,
                            function_project: ProjectFixture):
        request = UpdateProjectRequestSchema()
        response = projects_client.update_project_api(function_project.id, request)
        response_data = UpdateProjectResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_project_response(request, response_data)
        validate_json_schema(response.json(), UpdateProjectResponseSchema.model_json_schema())

    @allure.title("Delete project")
    def test_delete_project(self,
                            projects_client: ProjectsClient,
                            function_project: ProjectFixture):
        delete_response = projects_client.delete_project_api(function_project.id)
        assert_status_code(delete_response.status_code, HTTPStatus.NO_CONTENT)

        get_response = projects_client.get_project_api(function_project.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_project_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())
