import allure

from constants.locators import HomePageLocators
from constants.tags import Tags
from pom.page_factory.form import Form
from pom.page_factory.component import Component
from pom.page_factory.title import Title
from pom.pages.base_page import BasePage
from pom.models.page import Page
from utils.logger import logger


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.meta_description = Component(
            page, locator=HomePageLocators.META_DESCRIPTION, name="Meta tag"
        )

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
        self.page_title = Title(
            page, locator=HomePageLocators.HEADER_H1, name='Title'
        )
        self.page_header_h1 = Title(
            page, locator=HomePageLocators.HEADER_H1, name='Tag h1'
        )
        self.page_header_h2 = Title(
            page, locator=HomePageLocators.HEADER_H2, name='Tag h2'
        )
        self.page_header_h3 = Title(
            page, locator=HomePageLocators.HEADER_H3, name='Tag h3'
        )
        self.page_header_h3_quick_link = Title(
            page, locator=HomePageLocators.HEADER_H3_QUICK_LINK, name='Tag h3 Quick Link'
        )
        self.page_header_h3_widget = Title(
            page, locator=HomePageLocators.HEADER_H3_WIDGET, name='Tag h3 Widget'
        )
        self.footer_links = Component(
            page, locator=HomePageLocators.FOOTER_LINKS, name="Footer links"
        )

    @allure.step('Checking Meta tag')
    def check_meta_tag_robots(self, attribute: str, expected_value: str):
        self.meta_robots.should_have_attribute_value(attribute, expected_value)

    @allure.step('Checking Link canonical')
    def check_link_canonical(self, attribute: str, expected_value: str):
        self.link_canonical.should_have_attribute_value(attribute, expected_value)

    # @allure.step('Checking the Logo is visible')
    # def check_logo_is_visible(self):
    #     self.logo.should_be_visible()

    @allure.step('Checking the Search Form is visible')
    def check_search_form_is_visible(self):
        self.search_form.should_be_visible()

    @allure.step('Checking that the title of the browser page is "{expected_title_text}"')
    def check_browser_title(self, expected_title_text: str):
        self.page.check_browser_title(expected_title_text)

    @allure.step('Checking that the header tag/tags <{header_tag}> has/have text {expected_values}')
    def check_page_headers(self, header_tag: str, expected_values: tuple):
        if header_tag == Tags.H1:
            self.page_header_h1.should_have_values(expected_values)
        elif header_tag == Tags.H2:
            self.page_header_h2.should_have_values(expected_values)
        elif header_tag == Tags.H3:
            self.page_header_h3.should_have_values(expected_values, limits=4)
            self.page_header_h3_quick_link.get_elements().should().have_length(20)
            self.page_header_h3_widget.get_elements().should().have_length(3)
        else:
            logger.warning(f"No verification of the header {header_tag} is provided")

    @allure.step('Checking that the URL of the page is "{expected_url}"')
    def check_page_url(self, expected_url: str, errors: list):
        self.page.check_page_url(expected_url, self.errors)

    # @allure.step('Checking that Type in the Search form has a value "{expected_type_name}"')
    # def check_search_type(self, expected_type_name: str):
    #     self.search_form_type.should_have_text(expected_type_name)

    @allure.step('Checking that Search form is visible')
    def check_search_form_is_visible(self):
        self.search_form.should_be_visible()

    # @allure.step('Checking that the title of the page if "{expected_title_text}"')
    # def check_page_headers(self, expected_title_text: str):
    #     self.page_title.should_have_text(expected_title_text)

    @allure.step('Checking Footer links')
    def check_footer_links(self):
        links = self.page.find_xpath(HomePageLocators.FOOTER_LINKS)
        for index in range(links.length()):
            self.page.check_footer_link(index, HomePageLocators.FOOTER_LINKS, self.errors)

        if len(self.errors) > 0:
            with allure.step(f"As a result of checking Footer links, the following errors were detected:"):
                logger.warning("Detected Errors:")
                for error in self.errors:
                    with allure.step(error):
                        logger.warning(error)

    @allure.step('Checking Meta tag "description"')
    def check_meta_tag_description(self, attribute: str, expected_value: str):
        self.meta_description.should_have_attribute_value(attribute, expected_value)
