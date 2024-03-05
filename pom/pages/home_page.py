import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from constants.titles.titles import Titles
from constants.urls.routes import UIRoutes
from locators.home_page_locators import HomePageLocators
from constants.titles.navigation_menu import NavigationMenu
from constants.web_elements.tags import Tags
from pom.page_factory.button import Button
from pom.page_factory.component import Component
from pom.page_factory.title import Title
from pom.pages.base_page import BasePage
from pom.models.page import Page
from pom.pages.forms.search_form import SearchForm
from utils.logger import logger


class HomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.search_form = SearchForm(page)

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
        self.page_title = Title(
            page, locator=HomePageLocators.HEADER_H1, name='Title'
        )
        self.page_header_h1 = Title(
            page, locator=HomePageLocators.HEADER_H1, name='Tag h1'
        )
        self.page_header_h2 = Title(
            page, locator=HomePageLocators.HEADER_H2, name='Tag h2'
        )
        self.service_offerings_h3 = Title(
            page, locator=HomePageLocators.CAROUSEL_SERVICE_OFFERINGS_H3, name='Tag h3 Carousel service offerings'
        )
        self.page_header_h3_quick_link = Title(
            page, locator=HomePageLocators.HEADER_H3_QUICK_LINK, name='Tag h3 Quick Links'
        )
        self.page_header_h3_widget = Title(
            page, locator=HomePageLocators.HEADER_H3_WIDGET, name='Tag h3 Widget "Najnoviji blog postovi"'
        )
        self.footer_links = Component(
            page, locator=HomePageLocators.FOOTER_LINKS, name="Footer Links"
        )
        self.main_menu_button = Button(
            page, locator=HomePageLocators.MAIN_MENU_BUTTON, name="Main Menu Button"
        )
        self.menu_sale = Button(
            page, locator=HomePageLocators.MENU_SALE, name="Menu Button 'Prodaja'"
        )
        self.menu_rent = Button(
            page, locator=HomePageLocators.MENU_RENT, name="Menu Button 'Izdavanje'"
        )
        self.menu_new = Button(
            page, locator=HomePageLocators.MENU_NEW, name="Menu Button 'Novogradnja'"
        )
        self.menu_advertisement = Button(
            page, locator=HomePageLocators.MENU_ADVERTISEMENT, name="Menu Button 'Oglašavanje'"
        )
        self.login = Button(
            page, locator=HomePageLocators.LOGIN, name="Login Button"
        )
        self.login_dialog = Component(
            page, locator=HomePageLocators.LOGIN_DIALOG, name="Login Dialog"
        )
        self.blog_post_widget = Component(
            page, locator=HomePageLocators.BLOG_POST_WIDGET, name="Widget 'Najnoviji blog postovi'"
        )
        self.place_suggestions = Component(
            page, locator=HomePageLocators.PLACE_SUGGESTIONS, name="'Popularni gradovi' Quick Links"
        )
        self.carousel_service_offerings = Component(
            page, locator=HomePageLocators.CAROUSEL_SERVICE_OFFERINGS, name="Carousel 'Service Offerings'"
        )
        self.carousel_branding_agencies = Component(
            page, locator=HomePageLocators.CAROUSEL_BRANDING_AGENCIES, name="Carousel 'Istaknute Agencije'"
        )
        self.carousel_premium_ads = Component(
            page, locator=HomePageLocators.CAROUSEL_PREMIUM_ADS, name="Carousel 'Premijum oglasi'"
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

    @allure.step('Checking that the title of the browser page is "{expected_title_text}"')
    def check_browser_title(self, expected_title_text: str):
        self.page.check_browser_title(expected_title_text)

    @allure.step('Checking that the header tag/tags <{header_tag}> has/have text {expected_values}')
    def check_page_headers(self, header_tag: str, expected_values: tuple = (), expected_number: int = 0,
                           section: str = ""):
        if header_tag == Tags.H1:
            self.page_header_h1.should_be_visible()
            self.page_header_h1.should_have_values(expected_values)
        elif header_tag == Tags.H2:
            self.page_header_h2.should_be_visible()
            self.page_header_h2.should_have_values(expected_values)
        elif header_tag == Tags.H3:
            if section == Titles.WIDGET_TITLE:
                self.page_header_h3_widget.should_be_visible()
                self.page_header_h3_widget.get_elements().should().have_length(expected_number)
            elif section == "":
                self.service_offerings_h3.should_be_visible()
                self.service_offerings_h3.should_have_accessible_names(expected_values)
        else:
            logger.warning(f"No verification of the header {header_tag} is provided")

    @allure.step('Checking that the URL of the page is "{expected_url}"')
    def check_page_url(self, expected_url: str, errors: list = None):
        self.page.check_page_url(expected_url, errors)
        self.page.check_response_status_code()

    @allure.step('Checking that Search form is visible')
    def check_search_form_is_visible(self):
        self.search_form.form.should_be_visible()

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
        self.page.navigate_through_sub_menu(sub_menu)
        self.check_page_url(expected_url, self.errors)

    @allure.step('Login via email')
    def login_via_email(self):
        self.login.click()
        self.login_dialog.should_be_visible()

    @allure.step('Check Tabs "Prodaja/Izdavanje" are working')
    def check_tabs_are_working(self):
        self.search_form.click_rent_tab_and_check_attributes()
        self.search_form.click_sale_tab_and_check_attributes()

    @allure.step('Check Dropdowm "Tip" is working')
    def check_combobox_type(self):
        self.search_form.check_combobox_type()

    @allure.step('Search with parameters: "Cena do"={price_to}, "m2 od"={m2_from}')
    def search_with_parameters(self, property_type: str, price_to: str, m2_from: str):
        self.search_form.fill_in_search_form_and_click_search(property_type, price_to, m2_from)

    @allure.step('Check the Search returns no server errors')
    def check_the_search_returns_no_server_error(self, expected_path: str):
        self.page_header_h2.should_be_visible()
        self.page.check_page_url_has_path(expected_path)
        self.page.check_response_status_code()

    @allure.step('Check Widget "Najnoviji blog postovi" links')
    def check_blog_post_widget(self):
        self.blog_post_widget.should_be_visible()
        widget_links = self.page.find_xpath(HomePageLocators.BLOG_POST_WIDGET_LINKS)
        widget_links.should().not_be_empty()
        for index in range(widget_links.length()):
            self.page.check_link(index, HomePageLocators.BLOG_POST_WIDGET_LINKS)

    @allure.step('Check "Popularni gradovi" Quick Links')
    def check_place_suggestions(self):
        self.place_suggestions.should_be_visible()
        place_suggestions_buttons = self.page.find_xpath(HomePageLocators.PLACE_SUGGESTIONS_BUTTONS)
        for index in range(place_suggestions_buttons.length()):
            place_suggestions_button = self.page.find_xpath(HomePageLocators.PLACE_SUGGESTIONS_BUTTONS).list[index]
            place_suggestions_button.should().be_clickable()
            place_suggestions_button.click()
            self.page.check_page_url_has_path(UIRoutes.SALE_HOUSES)

    @allure.step('Check "Service offerings" Carousel Items')
    def check_carousel_service_offerings(self):
        self.carousel_service_offerings.should_be_visible()
        self.page.check_carousel_items(carousel_items_xpath=HomePageLocators.CAROUSEL_SERVICE_OFFERINGS_LINKS)

    @allure.step('Check "Istaknute Agencije" Carousel Items')
    def check_carousel_branding_agencies(self):
        self.carousel_branding_agencies.should_be_visible()
        self.page.check_carousel_items(carousel_items_xpath=HomePageLocators.CAROUSEL_BRANDING_AGENCIES_LINKS)

    @allure.step('Check "Premijum oglasi" Carousel Items')
    def check_carousel_premium_ads(self):
        self.carousel_premium_ads.should_be_visible()
        self.page.check_carousel_items(carousel_items_xpath=HomePageLocators.CAROUSEL_PREMIUM_ADS_LINKS)
