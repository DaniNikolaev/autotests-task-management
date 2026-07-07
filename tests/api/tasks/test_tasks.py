from http import HTTPStatus

import allure
import pytest

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.projects.projects_client import ProjectsClient
from api.clients.tasks.tasks_client import TasksClient
from api.clients.tasks.tasks_schema import CreateTaskRequestSchema, CreateTaskResponseSchema, GetTasksResponseSchema, \
    GetTaskResponseSchema, UpdateTaskRequestSchema, UpdateTaskResponseSchema
from api.fixtures.projects import ProjectFixture
from api.fixtures.tasks import TaskFixture
from tools.api.assertions.base import assert_status_code
from tools.api.assertions.schema import validate_json_schema
from tools.api.assertions.tasks import assert_create_task_response, assert_get_tasks_response, assert_get_task_response, \
    assert_update_task_response, assert_task_not_found_response


@pytest.mark.regression
@pytest.mark.tasks
class TestTasks:
    @allure.title("Create task")
    def test_create_task(self,
                         projects_client: ProjectsClient,
                         function_project: ProjectFixture):
        request = CreateTaskRequestSchema()
        response = projects_client.create_project_task_api(function_project.id, request)
        response_data = CreateTaskResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_task_response(request, response_data)
        validate_json_schema(response.json(), CreateTaskResponseSchema.model_json_schema())

    @allure.title("Get tasks")
    def test_get_tasks(self,
                       projects_client: ProjectsClient,
                       function_project: ProjectFixture,
                       function_task: TaskFixture):
        response = projects_client.get_project_tasks_api(function_project.id)
        response_data = GetTasksResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_tasks_response(response_data, [function_task.response])
        validate_json_schema(response.json(), GetTasksResponseSchema.model_json_schema())

    @allure.title("Get task")
    def test_get_task(self,
                      tasks_client: TasksClient,
                      function_task: TaskFixture):
        response = tasks_client.get_task_api(function_task.id)
        response_data = GetTaskResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_task_response(response_data, function_task.response)
        validate_json_schema(response.json(), GetTaskResponseSchema.model_json_schema())

    @allure.title("Update task")
    def test_update_task(self,
                         tasks_client: TasksClient,
                         function_task: TaskFixture):
        request = UpdateTaskRequestSchema()
        response = tasks_client.update_task_api(function_task.id, request)
        response_data = UpdateTaskResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_task_response(request, response_data)
        validate_json_schema(response.json(), GetTaskResponseSchema.model_json_schema())

    @allure.title("Delete task")
    def test_delete_task(self,
                         tasks_client: TasksClient,
                         function_task: TaskFixture):
        delete_response = tasks_client.delete_task_api(function_task.id)
        assert_status_code(delete_response.status_code, HTTPStatus.NO_CONTENT)

        get_response = tasks_client.get_task_api(function_task.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)
        assert_task_not_found_response(get_response_data)
        validate_json_schema(get_response.json(), InternalErrorResponseSchema.model_json_schema())
