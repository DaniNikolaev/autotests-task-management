import allure
from playwright.sync_api import Page, expect

from tools.logger import get_logger
from ui.elements.base_element import BaseElement


logger = get_logger("TEXTAREA")


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "textarea"

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Fill {self.type_of} "{self.name}" at index "{nth}" to value "{value}"'
        with allure.step(step):
            logger.info(step)
            locator.fill(value)

    def clear(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Clear {self.type_of} "{self.name}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            locator.clear()

    def check_have_attribute(self, name: str, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Check that {self.type_of} "{self.name}" at index "{nth}" has attribute "{name}"="{value}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_attribute(name, value)
