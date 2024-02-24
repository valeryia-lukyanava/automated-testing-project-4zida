from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pom.interfaces.element import ElementInterface
    from pom.interfaces.element_wait import ElementWaitInterface
    from pom.interfaces.page import PageInterface


class ElementShouldInterface(ABC):
    _page: "PageInterface"
    _wait: "ElementWaitInterface"
    _element: "ElementInterface"

    @abstractmethod
    def __init__(
            self,
            page: "PageInterface",
            element: "ElementInterface",
            timeout: int,
            ignored_exceptions: list = None
    ):
        ...

    @abstractmethod
    def be_clickable(self) -> "ElementInterface":
        ...

    @abstractmethod
    def be_hidden(self) -> "ElementInterface":
        ...

    @abstractmethod
    def be_visible(self) -> "ElementInterface":
        ...

    @abstractmethod
    def have_text(self, text: str, case_sensitive=True) -> "ElementInterface":
        ...

    @abstractmethod
    def have_attribute_value(self, attribute: str, value: str, case_sensitive=True, raise_error=True,
                             errors=None) -> "ElementInterface":
        ...
