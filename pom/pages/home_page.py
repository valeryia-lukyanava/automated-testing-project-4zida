import allure

from constants.locators import HomePageLocators
from pom.page_factory.form import Form
from pom.page_factory.component import Component
from pom.pages.base_page import BasePage
from pom.models.page import Page


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.meta_robots = Component(
            page, locator=HomePageLocators.META_ROBOTS, name="Meta tag"
        )
        self.link_canonical = Component(
            page, locator=HomePageLocators.LINK_CANONICAL, name="Link canonical"
        )
        # self.logo = Component(
        #     page, locator='//a[@title="Logo 4zida.rs"]', name="Logo 4zida.rs"
        # )
        self.search_form = Form(
            page, locator=HomePageLocators.SEARCH_FORM, name='Search form'
        )

    @allure.step('Checking Meta tag')
    def check_meta_tag(self, attribute: str, expected_value: str):
        self.meta_robots.should_have_attribute_value(attribute, expected_value)

    @allure.step('Checking Link canonical')
    def check_link_canonical(self, attribute: str, expected_value: str):
        self.link_canonical.should_have_attribute_value(attribute, expected_value)

    @allure.step('Checking the Logo is visible')
    def check_logo_is_visible(self):
        self.logo.should_be_visible()

    @allure.step('Checking the Search Form is visible')
    def check_search_form_is_visible(self):
        self.search_form.should_be_visible()

    @allure.step('Checking that the title of the browser page if "{expected_title_text}"')
    def check_browser_title(self, expected_title_text: str):
        self.page.check_browser_title(expected_title_text)

    # @allure.step('Checking that Type in the Search form has a value "{expected_type_name}"')
    # def check_search_type(self, expected_type_name: str):
    #     self.search_form_type.should_have_text(expected_type_name)

    @allure.step('Checking that Search form is visible')
    def check_search_form_is_visible(self):
        self.search_form.should_be_visible()

    # @allure.step('Checking that the title of the page if "{expected_title_text}"')
    # def check_page_title(self, expected_title_text: str):
    #     self.page_title.should_have_text(expected_title_text)
