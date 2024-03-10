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
            logger.info("The element is displayed and enabled (clickable)")
            return self._element

        raise AssertionError("The element was not clickable")

    def be_hidden(self) -> ElementInterface:
        """An expectation that the element is not displayed but still in the DOM (aka hidden)"""
        try:
            value = self._wait.until(lambda e: e and not e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            return self._element
        raise AssertionError("The element was not hidden")

    def be_visible(self) -> ElementInterface:
        """An expectation that the element is displayed"""
        try:
            value = self._wait.until(lambda e: e and e.is_displayed())
        except TimeoutException:
            value = False

        if value:
            logger.info("The element is visible")
            return self._element

        raise AssertionError("The element was not visible")

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
            f"The expected text: '{text}' - the actual text: '{self._element.web_element.text}'"
        )

    def have_accessible_name(self, accessible_name: str, case_sensitive=True) -> "ElementInterface":
        """An expectation that the element has the given accessible name"""
        try:
            if case_sensitive:
                value = self._wait.until(lambda e: e.accessible_name == accessible_name)
            else:
                value = self._wait.until(
                    lambda e: e.accessible_name.strip().lower() == accessible_name.lower()
                )
        except TimeoutException:
            value = False

        if value:
            return self._element

        raise AssertionError(
            f"The expected accessible name: '{accessible_name}' - The actual accessible name: "
            f"'{self._element.web_element.accessible_name}'"
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
            f"The expected attribute value: '{value}' - "
            f"The actual attribute value: '{self._element.web_element.get_attribute(attribute)}'"
        )
        if raise_error:
            raise error
        else:
            errors.append(str(error))

    def have_attribute(self, attribute) -> "ElementInterface":
        """An expectation that the element has the given attribute"""
        logger.info("The element should have an attribute '%s'", attribute)
        try:
            result = self._wait.until(lambda e: "" in e.get_attribute(attribute))
        except TimeoutException:
            result = False

        if result:
            return self._element

        raise AssertionError(f"The expected attribute '{attribute}' was not found")

    def not_have_attribute(self, attribute) -> "ElementInterface":
        """An expectation that the element has not the given attribute"""
        logger.info("Element should not have an attribute '%s'", attribute)
        try:
            result = not self._wait.until(lambda e: "" in e.get_attribute(attribute))
        except TypeError:
            result = True

        if result:
            return self._element

        raise AssertionError(f"The element should not have the attribute '{attribute}', but it was found")
