import allure

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.projects.projects_schema import CreateProjectRequestSchema, CreateProjectResponseSchema, ProjectSchema, \
    GetProjectsResponseSchema, GetProjectResponseSchema, UpdateProjectRequestSchema, UpdateProjectResponseSchema
from tools.api.assertions.base import assert_equal, assert_length
from tools.api.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("PROJECTS_ASSERTIONS")


@allure.step("Check project")
def assert_project(actual: ProjectSchema, expected: ProjectSchema):
    logger.info("Check project")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.owner_user_id, expected.owner_user_id, "owner_user_id")
    assert_equal(actual.created_at, expected.created_at, "created_at")
    assert_equal(actual.updated_at, expected.updated_at, "updated_at")


@allure.step("Check create project response")
def assert_create_project_response(request: CreateProjectRequestSchema,
                                   response: CreateProjectResponseSchema):
    logger.info("Check create project response")
    assert_equal(request.title, response.project.title, "title")
    assert_equal(request.description, response.project.description, "description")


@allure.step("Check update project response")
def assert_update_project_response(request: UpdateProjectRequestSchema,
                                   response: UpdateProjectResponseSchema):
    logger.info("Check update project response")
    assert_equal(request.title, response.project.title, "title")
    assert_equal(request.description, response.project.description, "description")


@allure.step("Check get projects response")
def assert_get_projects_response(get_projects_response: GetProjectsResponseSchema,
                                 create_project_responses: list[CreateProjectResponseSchema]):
    assert_length(get_projects_response.projects, create_project_responses, "projects")

    logger.info("Check get projects response")
    for i, create_project_response in enumerate(create_project_responses):
        assert_equal(get_projects_response.projects[i].id, create_project_response.project.id, "id")
        assert_equal(get_projects_response.projects[i].title, create_project_response.project.title, "title")
        assert_equal(get_projects_response.projects[i].description,
                     create_project_response.project.description, "description")
        assert_equal(get_projects_response.projects[i].owner_user_id,
                     create_project_response.project.owner_user_id, "owner_user_id")
        assert_equal(get_projects_response.projects[i].created_at,
                     create_project_response.project.created_at, "created_at")
        assert_equal(get_projects_response.projects[i].updated_at,
                     create_project_response.project.updated_at, "updated_at")


@allure.step("Check get project response")
def assert_get_project_response(get_project_response: GetProjectResponseSchema,
                                create_project_response: CreateProjectResponseSchema):
    logger.info("Check get project response")
    assert_project(get_project_response.project, create_project_response.project)


@allure.step("Check project not found response")
def assert_project_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(
        details="Project not found"
    )
    logger.info("Check project not found response")
    assert_internal_error_response(actual, expected)
