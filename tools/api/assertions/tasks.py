import allure

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.tasks.tasks_schema import TaskSchema, CreateTaskResponseSchema, CreateTaskRequestSchema, \
    GetTaskResponseSchema, GetTasksResponseSchema, UpdateTaskRequestSchema, UpdateTaskResponseSchema
from tools.api.assertions.base import assert_equal, assert_length
from tools.api.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("TASKS_ASSERTIONS")


@allure.step("Check task")
def assert_task(actual: TaskSchema, expected: TaskSchema):
    logger.info("Check task")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.priority, expected.priority, "priority")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")
    assert_equal(actual.related_project_id, expected.related_project_id, "related_project_id")
    assert_equal(actual.created_by_user_id, expected.created_by_user_id, "created_by_user_id")
    assert_equal(actual.created_at, expected.created_at, "created_at")
    assert_equal(actual.updated_at, expected.updated_at, "updated_at")


@allure.step("Check create task response")
def assert_create_task_response(request: CreateTaskRequestSchema,
                                response: CreateTaskResponseSchema):
    logger.info("Check create task response")
    assert_equal(request.title, response.task.title, "title")
    assert_equal(request.description, response.task.description, "description")
    assert_equal(request.status, response.task.status, "status")
    assert_equal(request.priority, response.task.priority, "priority")
    assert_equal(request.estimated_time, response.task.estimated_time, "estimated_time")


@allure.step("Check update task response")
def assert_update_task_response(request: UpdateTaskRequestSchema,
                                response: UpdateTaskResponseSchema):
    logger.info("Check update task response")
    assert_equal(request.title, response.task.title, "title")
    assert_equal(request.description, response.task.description, "description")
    assert_equal(request.status, response.task.status, "status")
    assert_equal(request.priority, response.task.priority, "priority")
    assert_equal(request.estimated_time, response.task.estimated_time, "estimated_time")


@allure.step("Check get task response")
def assert_get_task_response(get_task_response: GetTaskResponseSchema,
                             create_task_response: CreateTaskResponseSchema):
    logger.info("Check get task response")
    assert_task(get_task_response.task, create_task_response.task)


@allure.step("Check get tasks response")
def assert_get_tasks_response(get_tasks_response: GetTasksResponseSchema,
                              create_tasks_responses: list[CreateTaskResponseSchema]):
    assert_length(get_tasks_response.tasks, create_tasks_responses, "tasks")

    logger.info("Check get tasks response")
    for i, create_tasks_response in enumerate(create_tasks_responses):
        assert_equal(get_tasks_response.tasks[i].id,
                     create_tasks_response.task.id, "id")
        assert_equal(get_tasks_response.tasks[i].title,
                     create_tasks_response.task.title, "title")
        assert_equal(get_tasks_response.tasks[i].description,
                     create_tasks_response.task.description, "description")
        assert_equal(get_tasks_response.tasks[i].status,
                     create_tasks_response.task.status, "status")
        assert_equal(get_tasks_response.tasks[i].priority,
                     create_tasks_response.task.priority, "priority")
        assert_equal(get_tasks_response.tasks[i].estimated_time,
                     create_tasks_response.task.estimated_time, "estimated_time")
        assert_equal(get_tasks_response.tasks[i].related_project_id,
                     create_tasks_response.task.related_project_id, "related_project_id")
        assert_equal(get_tasks_response.tasks[i].created_by_user_id,
                     create_tasks_response.task.created_by_user_id, "created_by_user_id")
        assert_equal(get_tasks_response.tasks[i].created_at,
                     create_tasks_response.task.created_at, "created_at")
        assert_equal(get_tasks_response.tasks[i].updated_at,
                     create_tasks_response.task.updated_at, "updated_at")


@allure.step("Check task not found response")
def assert_task_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(
        details="Task not found"
    )
    logger.info("Check task not found response")
    assert_internal_error_response(actual, expected)
