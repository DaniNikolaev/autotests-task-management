import allure

from tools.logger import get_logger
from ui.elements.base_element import BaseElement


logger = get_logger("FILE_INPUT")


class FileInput(BaseElement):
    @property
    def type_of(self) -> str:
        return "File Input"

    def set_input_files(self, path: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        step = f'Set file "{path}" to the {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator.set_input_files(path)
