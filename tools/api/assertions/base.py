from typing import Any, Sized

import allure

from tools.logger import get_logger

logger = get_logger("BASE_ASSERTIONS")


@allure.step("Check that response status code equals to {expected}")
def assert_status_code(actual: int, expected: int):
    logger.info(f"Check that response status code equals to {expected}")
    assert actual == expected, (
        f'Incorrect response status code. '
        f'Expected status code: {expected}. '
        f'Actual status code: {actual}'
    )


@allure.step("Check that {name} equal to {expected}")
def assert_equal(actual: Any, expected: Any, name: str):
    logger.info(f"Check that {name} equal to {expected}")
    assert actual == expected, (
        f'Incorrect value: "{name}". '
        f'Expected value: {expected}. '
        f'Actual value: {actual}'
    )


@allure.step("Check that {name} is true")
def assert_is_true(actual: Any, name: str):
    logger.info(f"Check that {name} is true")
    assert actual, (
        f'Incorrect value: "{name}". '
        f'Expected true value but got: {actual}'
    )


def assert_length(actual: Sized, expected: Sized, name: str):
    step = f"Check that length of {name} equals to {len(expected)}"
    with allure.step(step):
        logger.info(step)
        assert len(actual) == len(expected), (
            f'Incorrect object length: "name". '
            f'Expected length: {len(expected)}. '
            f'Actual length: {len(actual)}'
        )
