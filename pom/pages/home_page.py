import allure

from constants.locators import HomePageLocators
from constants.navigation_menu import NavigationMenu
from constants.tags import Tags
from pom.page_factory.button import Button
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
        self.logo = Component(
            page, locator=HomePageLocators.LOGO, name="Logo"
        )
        self.search_form = Form(
            page, locator=HomePageLocators.SEARCH_FORM, name='Search Form'
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
            page, locator=HomePageLocators.FOOTER_LINKS, name="Footer Links"
        )
        self.main_menu_button = Button(
            page, locator=HomePageLocators.MAIN_MENU_BUTTON, name="Main Menu Button"
        )
        self.menu_sale = Button(
            page, locator=HomePageLocators.MENU_SALE, name="Menu Button"
        )
        self.menu_rent = Button(
            page, locator=HomePageLocators.MENU_RENT, name="Menu Button"
        )
        self.menu_new = Button(
            page, locator=HomePageLocators.MENU_NEW, name="Menu Button"
        )
        self.menu_advertisement = Button(
            page, locator=HomePageLocators.MENU_ADVERTISEMENT, name="Menu Button"
        )

        self.menu_elements = {
            NavigationMenu.MENU_SALE: self.menu_sale,
            NavigationMenu.MENU_RENT: self.menu_rent,
            NavigationMenu.MENU_NEW: self.menu_new,
            NavigationMenu.MENU_ADVERTISEMENT: self.menu_advertisement
        }

    @allure.step('Checking Meta tag')
    def check_meta_tag_robots(self, attribute: str, expected_value: str):
        self.meta_robots.should_have_attribute_value(attribute, expected_value)

    @allure.step('Checking Link canonical')
    def check_link_canonical(self, attribute: str, expected_value: str):
        self.link_canonical.should_have_attribute_value(attribute, expected_value)

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
    def check_page_url(self, expected_url: str, errors: list = None):
        self.page.check_page_url(expected_url, errors)
        self.page.check_response_status_code()

    # @allure.step('Checking that Type in the Search form has a value "{expected_type_name}"')
    # def check_search_type(self, expected_type_name: str):
    #     self.search_form_type.should_have_text(expected_type_name)

    @allure.step('Checking that Search form is visible')
    def check_search_form_is_visible(self):
        self.search_form.should_be_visible()

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

    @allure.step('Check if external links have an attribute rel="nofollow">')
    def check_external_links(self, expected_external_links: list, attribute: str, expected_value: str) -> list:
        external_links = self.page.find_xpath(HomePageLocators.FOOTER_LINKS)
        expected_external_links_list = expected_external_links.copy()
        for index in range(external_links.length()):
            self.page.check_external_link(index, HomePageLocators.FOOTER_LINKS, expected_external_links_list, attribute,
                                          expected_value, self.errors)
        if len(expected_external_links_list) > 0:
            self.errors.append(f"The next external links have not been found on the page: "
                               f"{expected_external_links_list}")
            logger.info(self.errors[-1])
        return self.errors

    @allure.step('Checking Meta tag "description"')
    def check_meta_tag_description(self, attribute: str, expected_value: str):
        self.meta_description.should_have_attribute_value(attribute, expected_value)

    @allure.step('Checking Menu navigation: "{menu}" > "{sub_menu}"')
    def check_menu_navigation(self, menu: str, sub_menu: str, expected_url: str):
        self.main_menu_button.should_be_visible()
        self.main_menu_button.click()
        menu_element = self.menu_elements[menu]
        menu_element.should_be_visible()
        menu_element.click()
        self.page.sub_menu_navigate(sub_menu)
        self.check_page_url(expected_url)
