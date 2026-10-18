from ui.elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "Text"

    def check_have_placeholder(self, expected_placeholder: str, nth: int = 0, **kwargs):
        self.check_have_attribute("placeholder", expected_placeholder, nth, **kwargs)