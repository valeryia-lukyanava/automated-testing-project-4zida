from typing import Union

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from pom.interfaces.page import PageInterface
from pom.interfaces.page_wait import (PageWaitInterface, WebDriverUntilMethod)
from pom.models.element import Element
from pom.models.elements import Elements


class PageWait(PageWaitInterface):
    def __init__(
            self,
            page: PageInterface,
            webdriver: WebDriver,
            timeout: int,
            ignored_exceptions: tuple | None = None
    ):
        self._page = page
        self._webdriver = webdriver
        self._wait = WebDriverWait(
            driver=webdriver,
            timeout=timeout,
            ignored_exceptions=ignored_exceptions
        )

    def until(self, method: WebDriverUntilMethod, message=""):
        value = self._wait.until(method, message)

        if isinstance(value, WebElement):
            return Element(self._page, value, None)

        if isinstance(value, list):
            return Elements(self._page, value, None)

        return value

    def until_not(self, method: WebDriverUntilMethod, message=""):
        value = self._wait.until_not(method, message)

        if isinstance(value, WebElement):
            return Element(self._page, value, None)

        if isinstance(value, list):
            return Elements(self._page, value, None)

        return value

    def build(
            self, timeout: int, use_self=False, ignored_exceptions: list = None
    ) -> Union[WebDriverWait, "PageWait"]:
        if use_self:
            return PageWait(self._page, self._webdriver, timeout, ignored_exceptions)

        return WebDriverWait(self._webdriver, timeout, ignored_exceptions=ignored_exceptions)
