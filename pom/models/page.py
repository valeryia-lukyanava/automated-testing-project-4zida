import time
from datetime import datetime

import allure
import requests
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.exceptions import MaxRetryError

from config import UIConfig
from constants.attributes import Attributes
from constants.js_scripts import JS
from constants.routes import UIRoutes
from utils.bowser_log_parser import get_lcp_from_logs
from utils.logger import logger
from pom.interfaces.page import PageInterface
from pom.models.element import Element
from pom.models.elements import Elements
from pom.models.page_wait import PageWait
from webdriver.factory.factory import build_from_config


class Page(PageInterface):
    """
    Page interface that representing interactions with page like finding locators, opening url etc.
    """

    def __init__(self, config: UIConfig):
        self.config = config
        self._webdriver = None
        self._wait = None

    def init_webdriver(self) -> WebDriver:
        """Initialize WebDriver using the UIConfig"""
        self._webdriver = build_from_config(self.config)

        self._wait = PageWait(
            self, self._webdriver, self.config.driver.wait_time, ignored_exceptions=None
        )

        if self.config.driver.page_load_wait_time:
            self.set_page_load_timeout(self.config.driver.page_load_wait_time)

        if self.config.viewport.maximize:
            self.maximize_window()
        else:
            self.viewport(
                self.config.viewport.width,
                self.config.viewport.height,
                self.config.viewport.orientation
            )
        logger.info(f"User Agent: {self._webdriver.execute_script(JS.USER_AGENT)}")
        return self._webdriver

    @property
    def webdriver(self) -> WebDriver:
        """The current instance of Selenium's 'WebDriver' API."""
        return self.init_webdriver() if self._webdriver is None else self._webdriver

    def url(self) -> str:
        """Get the current page's URL"""
        return self.webdriver.current_url

    def title(self) -> str:
        """Get the current page's title"""
        return self.webdriver.title

    def get(self, url: str) -> "Page":
        """Navigate to the given URL"""
        self.get_page_by_url(url)
        return self

    def get_performance_metrics(self, run: int, performance_metrics: dict) -> "Page":
        """Measure the Performance"""
        logger.info(f"Measuring performance metrics: run №{run}")
        logger.info("Document Ready State: %s", self.webdriver.execute_script(JS.DOCUMENT_READY_STATE))

        page_load_time = self.webdriver.execute_script(JS.PAGE_LOAD_TIME)
        logger.info(f"Page Load Time: {page_load_time}")

        ttfb = self.webdriver.execute_script(JS.TTFB)
        logger.info(f"TTFB: {ttfb}")

        endtoend_response_time = self.webdriver.execute_script(JS.ENDTOEND_RESPONSE_TIME)
        logger.info(f"End-to-End Response Time: {endtoend_response_time}")

        self.webdriver.execute_script(JS.CONSOLE_CLEAR)
        self.webdriver.execute_script(JS.LCP)
        lcp = get_lcp_from_logs(self.webdriver.get_log('browser'))
        logger.info(f"Largest Contentful Paint: {lcp}")

        metrics = {"URL": self.webdriver.current_url,
                   "TTFB": ttfb,
                   "LCP": lcp,
                   "PageLoadTime": page_load_time,
                   "EndToEndResponseTime": endtoend_response_time}
        performance_metrics[str(datetime.now())] = metrics

        return self

    def get_page_by_url(self, url):
        """Navigate to the given URL"""
        normalized_url = url if url.startswith('http') else (self.config.base_url + url)
        logger.info("Page.visit() - Get URL: '%s'", normalized_url)
        # time.sleep(0.5)
        self.webdriver.get(normalized_url)
        logger.info(f"Client window width: {self._webdriver.execute_script(JS.CLIENT_WINDOW_WIDTH)}, window height: "
                    f"{self._webdriver.execute_script(JS.CLIENT_WINDOW_HEIGHT)}")

    def reload(self) -> "Page":
        """Reload (aka refresh) the current window"""
        logger.info("Page.reload() - Reloading the page")

        self.webdriver.refresh()
        return self

    def wait_until_stable(self) -> WebDriver:
        """Waits until webdriver will be stable"""
        logger.info("Page.wait_until_stable() - Page wait until driver stable")

        try:
            return self.webdriver
        except MaxRetryError:
            time.sleep(1)
            self.wait_until_stable()

    def get_xpath(self, xpath: str, timeout: int = None) -> Element:
        """
        Finds the DOM element that match the XPATH selector.

        * If 'timeout=None' (default), use the default wait_time.
        * If 'timeout > 0', override the default wait_time.
        * If 'timeout=0', poll the DOM immediately without any waiting.
        """
        logger.info(
            "Page.get_xpath() - Get the element with xpath: '%s'", xpath
        )

        by = By.XPATH

        if timeout == 0:
            element = self.webdriver.find_element(by, xpath)
        else:
            element = self.wait(timeout).until(
                lambda x: x.find_element(by, xpath),
                f"Could not find an element with xpath: '{xpath}'"
            )

        return Element(self, element, locator=(by, xpath))

    def find_xpath(self, xpath: str, timeout: int = None) -> Elements:
        """
        Finds the DOM elements that match the XPATH selector.

        * If 'timeout=None' (default), use the default wait_time.
        * If 'timeout > 0', override the default wait_time.
        * If 'timeout=0', poll the DOM immediately without any waiting.
        """
        by = By.XPATH
        elements: list[WebElement] = []

        logger.info(
            "Page.find_xpath() - Get the elements with xpath: '%s'", xpath
        )

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, xpath),
                    f"Could not find an element with xpath: '{xpath}'"
                )
        except TimeoutException:
            pass

        return Elements(self, elements, locator=(by, xpath))

    def wait(
            self, timeout: int = None, use_self: bool = False, ignored_exceptions: list = None
    ) -> WebDriverWait | PageWait:
        """The Wait object with the given timeout in seconds"""
        if timeout:
            return self._wait.build(timeout, use_self, ignored_exceptions)

        return self._wait.build(self.config.driver.wait_time, use_self, ignored_exceptions)

    def quit(self):
        """Quits the driver"""
        logger.info(
            "Page.quit() - Quit page and close all windows from the browser session"
        )

        self.webdriver.quit()

    def screenshot(self, filename: str) -> str:
        """Take a screenshot of the current Window"""
        logger.info("Page.screenshot() - Save screenshot to: '%s'", filename)

        self.webdriver.save_screenshot(filename)
        return filename

    def maximize_window(self) -> "Page":
        """Maximizes the current Window"""
        logger.info("Page.maximize_window() - Maximize browser window")

        self.webdriver.maximize_window()
        return self

    def execute_script(self, script: str, *args) -> "Page":
        """Executes javascript in the current window or frame"""
        logger.info(
            "Page.execute_script() - Execute javascript '%s' into the Browser", script
        )

        self.webdriver.execute_script(script, *args)
        return self

    def set_page_load_timeout(self, timeout: int) -> "Page":
        """Set the amount of time to wait for a page load to complete before throwing an error"""
        logger.info(
            "Page.set_page_load_timeout() - Set page load timeout: '%s'", timeout
        )

        self.webdriver.set_page_load_timeout(timeout)
        return self

    def viewport(self, width: int, height: int, orientation: str = "portrait") -> "Page":
        """Control the size and orientation of the current context's browser window"""
        logger.info(
            "Page.viewport() - Set viewport width: '%s', height: '%s', orientation: '%s'",
            width, height, orientation
        )

        if orientation == "portrait":
            self.webdriver.set_window_size(width, height)
        elif orientation == "landscape":
            self.webdriver.set_window_size(height, width)
        else:
            raise ValueError("Orientation must be 'portrait' or 'landscape'.")
        return self

    def check_browser_title(self, title_name):
        """Check the title of the browser page"""
        value = None
        try:
            actual_title = self.title()
            logger.info("The title of the page is '%s'", actual_title)
            if actual_title == title_name:
                value = True
        except TimeoutException:
            value = False

        if value:
            return self.title()

        raise AssertionError(
            f"Expected title: '{title_name}' - Actual text: '{self.title()}'"
        )

    def check_page_headers(self, title_name):
        """Check the title of the page"""
        value = None
        try:
            actual_title = self.title()
            logger.info("The title of the page is '%s'", actual_title)
            if actual_title == title_name:
                value = True
        except TimeoutException:
            value = False

        if value:
            return self.title()

        raise AssertionError(
            f"Expected title: '{title_name}' - Actual text: '{self.title()}'"
        )

    def check_page_url(self, url, errors):
        """Check the URL of the page"""
        try:
            value = self._wait.until(lambda e: e.current_url == url)
            actual_url = self.url()
            logger.info("The URL of the page is '%s'", actual_url)
            if actual_url == url:
                value = True
        except TimeoutException:
            value = False

        if value:
            return self.url()
        else:
            errors.append(AssertionError(f"Expected URL: '{url}' - Actual URL: '{self.url()}'"))
            logger.error(f"Expected URL: '{url}' - Actual URL: '{self.url()}'")

    def check_web_element_located(self, xpath: str, timeout: int = None) -> bool:
        """Check the web element is located"""
        by = By.XPATH
        elements: list[WebElement] = []
        logger.info(f"Page.find_xpath() - Get the elements with xpath: {xpath}")

        try:
            if timeout == 0:
                elements = self.webdriver.find_elements(by, xpath)
            else:
                elements = self.wait(timeout).until(
                    lambda x: x.find_elements(by, xpath),
                    f"Could not find an element with xpath: '{xpath}'"
                )
        except TimeoutException:
            pass

        if len(elements):
            return True

        raise AssertionError(
            f"Expected result: the element with XPath = '{xpath}' is located, Actual result: the element is not found"
        )

    def check_footer_link(self, index, locator, errors):

        link = self.find_xpath(locator).list[index]
        url = link.web_element.get_attribute(Attributes.HREF)
        text = link.web_element.text
        if text == '':
            image = self.webdriver.find_elements(By.XPATH, f"({locator})[{index + 1}]//img")
            if len(image) > 0:
                text = image[0].get_attribute('alt')

        if url != UIRoutes.MAILTO:
            with allure.step(f"Checking Footer link #{index} '{text}' (href = '{url}')"):

                logger.info(f"Link #{index} '{text}' (href = '{url}')")
                link.should().be_clickable()

                if self.config.api_check_links:
                    response = requests.get(url=url,
                                            headers={"IC-Bypass-Throttling": "8f190c31363e1d3a08ec0ccd0eed4be4"},
                                            timeout=60)
                    response_status_code = response.status_code
                    response_ulr = response.url
                    logger.info(f"GET '{url}'. Response status code: {response_status_code}")

                    if int(response_status_code) >= 400:
                        errors.append(str(AssertionError(f"Link #{index} '{text}', GET '{url}'. "
                                                         f"Expected status code should be < 400. "
                                                         f"Actual status code: '{response_status_code}'")))

                    if response_ulr != url:
                        errors.append(str(AssertionError(f"Link #{index} '{text}'. "
                                                         f"Footer link attribute 'href': {url}"
                                                         f"Response URL: '{response_ulr}'")))
                else:
                    try:
                        link.click()
                    except StaleElementReferenceException:
                        link.click()
                    logger.info(f"Clicked Footer link #{index} '{text}', 'href'={url}")

                    window_handlers = self.webdriver.window_handles
                    if len(window_handlers) > 1:
                        self.webdriver.switch_to.window(window_handlers[len(window_handlers) - 1])
                    self.check_page_url(url=url, errors=errors)

                    self.get(self.config.base_url)
                    # To avoid Error 429
                    time.sleep(3)

    def check_external_link(self, index: int, locator: str, expected_external_links: list, attribute: str,
                            expected_value: str, errors: list):
        link = self.find_xpath(locator).list[index]
        url = link.web_element.get_attribute(Attributes.HREF)
        if url in expected_external_links:
            with allure.step(f"Checking Footer link #{index} href = '{url}'"):
                logger.info(f"Link #{index} href = '{url}'")
                errors_len = len(errors)
                link.should().have_attribute_value(attribute, expected_value, raise_error=False, errors=errors)
                if len(errors) > errors_len:
                    errors[-1] = f"Link #{index} href = '{url}' {errors[-1]}"
                    logger.info(errors[-1])
                expected_external_links.remove(url)
