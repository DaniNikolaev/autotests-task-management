import allure
from typing import Union

from tools.logger import get_logger
from ui.elements.base_element import BaseElement

logger = get_logger("SELECT")


class Select(BaseElement):
    @property
    def type_of(self) -> str:
        return "Select"

    def select_by_value(self, value: str, nth: int = 0, **kwargs):
        """
        Выбирает опцию по атрибуту value (самый надежный способ).
        Пример: select_by_value("in_progress")
        """
        locator = self.get_locator(nth, **kwargs)
        step = f'Selecting option by value "{value}" in {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator.select_option(value=value)

    def select_by_label(self, label: str, nth: int = 0, **kwargs):
        """
        Выбирает опцию по видимому тексту (label).
        Пример: select_by_label("In Progress")
        """
        locator = self.get_locator(nth, **kwargs)
        step = f'Selecting option by label "{label}" in {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator.select_option(label=label)

    def select_by_index(self, index: int, nth: int = 0, **kwargs):
        """
        Выбирает опцию по порядковому номеру (начиная с 0).
        Используется редко, только если нет стабильных value или label.
        """
        locator = self.get_locator(nth, **kwargs)
        step = f'Selecting option by index "{index}" in {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator.select_option(index=index)

    def get_selected_value(self, nth: int = 0, **kwargs) -> str:
        """
        Возвращает атрибут value выбранной в данный момент опции.
        """
        locator = self.get_locator(nth, **kwargs)
        step = f'Getting selected value from {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            return locator.input_value()

    def get_selected_label(self, nth: int = 0, **kwargs) -> str:
        """
        Возвращает видимый текст (label) выбранной в данный момент опции.
        """
        locator = self.get_locator(nth, **kwargs)
        step = f'Getting selected label from {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            # Находим выбранную опцию внутри селекта и берем её текст
            return locator.locator("option:checked").inner_text()
