from typing import Any, List, Union

import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, parent: Union[Page, Locator], locator: str, name: str):
        self.parent = parent
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return "base_element"

    def get_raw_locator(self, nth: int = 0, **kwargs):
        locator = self.locator.format(**kwargs)
        return f"//*[@data-testid='{locator}'][{nth+1}]"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with data-testid="{locator}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            return self.parent.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Clicking {self.type_of} "{self.name}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is visible'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has text "{text}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_text(text)

    def check_have_text_from_list(self, texts: List[str], nth: int = 0, ** kwargs):
        locator = self.get_locator(nth, **kwargs)
        for text in texts:
            step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has text "{text}"'
            with allure.step(step):
                logger.info(step)
                try:
                    expect(locator).to_have_text(text)
                    break
                except:
                    continue

    def check_have_value(self, value: Any, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" has value "{value}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_value(value)

    def check_have_attribute(self, attribute_name: str, expected_value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        value_str = f'"{expected_value}"' if expected_value is not None else ""
        step = f'Checking that {self.type_of} "{self.name}" has attribute "{attribute_name}" = {value_str}'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_attribute(attribute_name, expected_value)
