import allure
from playwright.sync_api import expect

from tools.logger import get_logger
from ui.elements.base_element import BaseElement

logger = get_logger("LINK")


class Link(BaseElement):
    @property
    def type_of(self) -> str:
        return "LINK"

    def check_have_attribute(self, name: str, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Check that {self.type_of} "{self.name}" at index "{nth}" has attribute "{name}"="{value}"'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_attribute(name, value)
