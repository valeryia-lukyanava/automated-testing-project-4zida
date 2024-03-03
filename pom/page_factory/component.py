import allure
from selenium.common.exceptions import StaleElementReferenceException
from pom.models.element import Element
from pom.models.elements import Elements
from pom.models.page import Page
from utils.logger import logger


class Component:
    def __init__(self, page: Page, locator: str, name: str) -> None:
        self._page = page
        self._locator = locator
        self._name = name

    @property
    def type_of(self) -> str:
        return 'component'

    @property
    def name(self) -> str:
        return self._name

    def get_element(self, **kwargs) -> Element:
        locator = self._locator.format(**kwargs)
        with allure.step(f'Getting {self.type_of} with the name "{self.name}" and the locator "{locator}"'):
            return self._page.get_xpath(locator)

    def get_elements(self, **kwargs) -> Elements:
        locator = self._locator.format(**kwargs)
        with allure.step(f'Getting {self.type_of}s with the name "{self.name}" and the locator "{locator}"'):
            return self._page.find_xpath(locator)

    def click(self, **kwargs) -> None:
        with allure.step(f'Clicking {self.type_of} with name "{self.name}"'):
            element = self.get_element(**kwargs)
            element.scroll_to_element().click()

    def should_be_visible(self, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" is visible'):
            try:
                element = self.get_element(**kwargs)
                element.scroll_to_element()
                element.should().be_visible()
            except StaleElementReferenceException:
                self.should_be_visible(**kwargs)

    def should_have_text(self, text: str, **kwargs) -> None:
        with allure.step(f'Checking that {self.type_of} "{self.name}" has a text "{text}"'):
            try:
                element = self.get_element(**kwargs)
                element.should().have_text(text)
            except StaleElementReferenceException:
                self.should_have_text(text, **kwargs)

    def should_have_values(self, values: tuple, limits: int = 0, **kwargs) -> None:
        elements = self.get_elements(**kwargs)
        actual_text_values = [element.web_element.text for element in elements.list]
        n = limits if limits > 0 else len(elements.list)
        logger.info(f"Actual headers text: {actual_text_values[0:n]}")
        for i in range(0, n):
            with allure.step(f'Checking that header tag "{elements.list[i].web_element.tag_name}" has text: '
                             f'"{values[i]}"'):
                try:
                    elements.list[i].should().have_text(values[i])
                except StaleElementReferenceException:
                    elements.list[i].should().have_text(values[i])

    def is_displayed(self, **kwargs) -> bool:
        with allure.step(f'Checking if {self.type_of} "{self.name}" is visible'):
            element = self.get_element(**kwargs)
            return element.is_displayed()

    def should_have_attribute_value(self, attribute, value, **kwargs):
        with allure.step(f'Checking that {self.type_of} has an attribute "{attribute}" with a value "{value}"'):
            try:
                element = self.get_element(**kwargs)
                element.should().have_attribute_value(attribute, value)
            except StaleElementReferenceException:
                self.should_have_attribute_value(attribute, value, **kwargs)

    def should_have_attribute(self, attribute, **kwargs):
        with allure.step(f'Checking that {self.type_of} has an attribute "{attribute}"'):
            try:
                element = self.get_element(**kwargs)
                element.should().have_attribute(attribute)
            except StaleElementReferenceException:
                self.should_have_attribute(attribute, **kwargs)
