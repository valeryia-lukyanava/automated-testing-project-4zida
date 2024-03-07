from selenium.webdriver.remote.webdriver import WebElement

from pom.interfaces.element import ElementInterface
from pom.interfaces.elements import ElementsInterface
from pom.interfaces.page import PageInterface
from pom.models.elements_should import ElementsShould


class Elements(ElementsInterface):

    def __init__(
        self,
        page: PageInterface,
        web_elements: list[WebElement],
        locator: tuple[str, str] | None
    ):
        from pom.models.element import Element

        self._page = page
        self.list: list[ElementInterface] = [
            Element(page, element, None) for element in web_elements
        ]
        self.locator = locator

    def length(self) -> int:
        return len(self.list)

    def is_empty(self) -> bool:
        """Checks if there are zero elements in the list."""
        return self.length() == 0

    def should(self, timeout: int = 0, ignored_exceptions: list = None) -> ElementsShould:
        if timeout:
            wait_time = timeout
        else:
            wait_time = self._page.config.driver.wait_time
        return ElementsShould(self._page, self, wait_time, ignored_exceptions)
