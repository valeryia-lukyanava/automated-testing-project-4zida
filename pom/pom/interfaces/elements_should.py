from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Union

from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    from pom.interfaces.elements import ElementsInterface
    from pom.interfaces.page import PageInterface
    from pom.interfaces.page_wait import PageWaitInterface


class ElementsShouldInterface(ABC):
    _page: "PageInterface"
    _wait: Union[WebDriverWait, "PageWaitInterface"]
    _elements: "ElementsInterface"

    @abstractmethod
    def __init__(
            self,
            page: "PageInterface",
            elements: "ElementsInterface",
            timeout: int,
            ignored_exceptions: list = None
    ):
        ...

    @abstractmethod
    def have_length(self, length: int) -> bool:
        ...

    @abstractmethod
    def not_be_empty(self) -> "ElementsInterface":
        ...
