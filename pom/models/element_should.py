from selenium.common.exceptions import TimeoutException

from utils.logger import logger
from pom.interfaces.element import ElementInterface
from pom.interfaces.element_should import ElementShouldInterface
from pom.interfaces.page import PageInterface
from pom.models.element_wait import ElementWait


class ElementShould(ElementShouldInterface):
    """ElementShould API: Commands (aka Expectations) for the current Element"""

    def __init__(
            self,
            page: PageInterface,
            element: ElementInterface,
            timeout: int,
            ignored_exceptions: list = None
    ):
        self._page = page
        self._element = element
        self._wait = ElementWait(
            element.web_element, timeout, ignored_exceptions
        )

    def be_clickable(self) -> ElementInterface:
        """An expectation that the element is displayed and enabled so you can click it"""
        try:
            value = self._wait.until(
                lambda e: e.is_displayed() and e.is_enabled()
            )
        except TimeoutException:
            value = False
        if value:
            logger.info("Element is displayed and enabled (clickable)")
            return self._element

        raise AssertionError("Element was not clickable")

    def be_hidden(self) -> ElementInterface:
        """An expectation that the element is not displayed but still in the DOM (aka hidden)"""
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        raise AssertionError("Element was not hidden")

    def be_visible(self) -> ElementInterface:
        """An expectation that the element is displayed"""
        try:
            value = self._wait.until(lambda e: e and e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element

        raise AssertionError("Element was not visible")

    def have_text(self, text: str, case_sensitive=True) -> "ElementInterface":
        """An expectation that the element has the given text"""
        try:
            if case_sensitive:
                value = self._wait.until(lambda e: e.text == text)
            else:
                value = self._wait.until(
                    lambda e: e.text.strip().lower() == text.lower()
                )
        except TimeoutException:
            value = False

        if value:
            return self._element

        raise AssertionError(
            f"Expected text: '{text}' - Actual text: '{self._element.web_element.text}'"
        )

    def have_attribute_value(self, attribute: str, value: str, case_sensitive=True, raise_error=True,
                             errors=None) -> "ElementInterface":
        """An expectation that the element has the given value for the attribute"""
        logger.info("Element should have an attribute '%s' with a value '%s'", attribute, value)
        try:
            if case_sensitive:
                result = self._wait.until(lambda e: value in e.get_attribute(attribute))
            else:
                result = self._wait.until(
                    lambda e: value.lower() in e.get_attribute(attribute).strip().lower()
                )
        except TimeoutException:
            result = False

        if result:
            return self._element

        error = AssertionError(
            f"Expected attribute value: '{value}' - "
            f"Actual attribute value: '{self._element.web_element.get_attribute(attribute)}'"
        )
        if raise_error:
            raise error
        else:
            errors.append(str(error))
