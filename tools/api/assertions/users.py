import allure

from api.clients.errors_schema import InternalErrorResponseSchema
from api.clients.users.users_schema import UserSchema, CreateUserRequestSchema, CreateUserResponseSchema, \
    UpdateUserRequestSchema, UpdateUserResponseSchema, GetUserResponseSchema
from tools.api.assertions.base import assert_equal
from tools.api.assertions.errors import assert_internal_error_response
from tools.logger import get_logger

logger = get_logger("USER_ASSERTIONS")


@allure.step("Check user")
def assert_user(actual_user: UserSchema, expected_user: UserSchema):
    logger.info("Check user")
    assert_equal(actual_user.id, expected_user.id, "id")
    assert_equal(actual_user.email, expected_user.email, "email")
    assert_equal(actual_user.last_name, expected_user.last_name, "last name")
    assert_equal(actual_user.first_name, expected_user.first_name, "first name")
    assert_equal(actual_user.created_at, expected_user.created_at, "created at")
    assert_equal(actual_user.update_at, expected_user.update_at, "updated at")
    assert_equal(actual_user.is_active, expected_user.is_active, "is active")


@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestSchema,
                                response: CreateUserResponseSchema):
    logger.info("Check create user response")
    assert_equal(request.email, response.user.email, "email")
    assert_equal(request.last_name, response.user.last_name, "last name")
    assert_equal(request.first_name, response.user.first_name, "first name")


@allure.step("Check update user response")
def assert_update_user_response(request: UpdateUserRequestSchema,
                                response: UpdateUserResponseSchema):
    logger.info("Check update user response")
    assert_equal(request.email, response.user.email, "email")
    assert_equal(request.last_name, response.user.last_name, "last name")
    assert_equal(request.first_name, response.user.first_name, "first name")


@allure.step("Check get user response")
def assert_get_user_response(create_user_request: CreateUserRequestSchema,
                             get_user_response: GetUserResponseSchema):
    logger.info("Check get user response")
    assert_equal(create_user_request.email, get_user_response.user.email, "email")
    assert_equal(create_user_request.last_name, get_user_response.user.last_name, "last name")
    assert_equal(create_user_request.first_name, get_user_response.user.first_name, "first name")


@allure.step("Check user not found response")
def assert_user_not_found_response(actual: InternalErrorResponseSchema):
    expected = InternalErrorResponseSchema(
        details="User not found"
    )
    logger.info("Check user not found response")
    assert_internal_error_response(actual, expected)
