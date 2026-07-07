import allure

from tools.logger import get_logger
from ui.elements.base_element import BaseElement

logger = get_logger("INPUT")


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "Input"

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
            