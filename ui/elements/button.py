import allure
from playwright.sync_api import expect

from tools.logger import get_logger
from ui.elements.base_element import BaseElement


logger = get_logger("BUTTON")


class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "Button"

    def check_disabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is disabled'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Checking that {self.type_of} "{self.name}" at index "{nth}" is enabled'
        with allure.step(step):
            logger.info(step)
            expect(locator).to_be_enabled()
