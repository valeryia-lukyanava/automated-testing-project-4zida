import allure
import pytest
from flaky import flaky

from constants.web_elements.attributes import Attributes
from constants.urls.external_links import ExternalLinks
from constants.titles.headers import Headers
from constants.web_elements.tags import Tags
from pom.pages.home_page import HomePage
from constants.titles.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@pytest.mark.chrome_mobile
@pytest.mark.seo
@pytest.mark.order(3)
@flaky(max_runs=2)
@allure.severity(allure.severity_level.NORMAL)
@allure.suite(Suite.SEO)
class TestSEO:
    @allure.id('1')
    @allure.title('Check Browser Page Title')
    def test_browser_title(self, home_page: HomePage):
        home_page.visit()
        # Assert page title
        home_page.check_browser_title(expected_title_text=Titles.HOME_PAGE_BROWSER_TITLE)

    @allure.id('2')
    @allure.title('Check Meta Tags')
    def test_meta_tags(self, home_page: HomePage):
        home_page.visit()
        # Assert meta tags
        home_page.check_meta_tag_description(attribute="content",
                                             expected_value=Titles.META_DESCRIPTION)

    @allure.id('3')
    @allure.title('Check Page Header Tag <h1>')
    def test_h1_tag(self, home_page: HomePage):
        home_page.visit()
        # Assert h1
        home_page.check_page_headers(header_tag=Tags.H1,
                                     expected_values=Headers.H1)

    @allure.id('4')
    @allure.title('Check Page Header Tags <h2>')
    def test_h2_tags(self, home_page: HomePage):
        home_page.visit()
        # Expected h2 tags
        home_page.check_page_headers(header_tag=Tags.H2,
                                     expected_values=Headers.H2)

    @allure.id('5')
    @allure.title('Check Page Header Tags <h3> in Carousel Added Values')
    def test_h3_tags_carousel_added_values(self, home_page: HomePage):
        home_page.visit()
        # Expected h3 tags
        home_page.check_page_headers(header_tag=Tags.H3,
                                     expected_values=Headers.SERVICE_OFFERINGS_H3)

    @allure.id('6')
    @allure.title('Check Page Header Tags <h3> in section "Najnoviji blog postovi" Widget')
    def test_h3_tags_widget(self, home_page: HomePage):
        home_page.visit()
        # Expected h3 tags
        home_page.check_page_headers(header_tag=Tags.H3,
                                     section=Titles.WIDGET_TITLE,
                                     expected_number=3)

    @allure.id('7')
    @allure.title('Check if external links have an attribute rel="nofollow"')
    def test_external_links(self, home_page: HomePage):
        home_page.visit()
        # Check if external links have a tag rel="nofollow">
        errors = home_page.check_external_links(expected_external_links=ExternalLinks.ExternalLinksList,
                                                attribute=Attributes.REL,
                                                expected_value="nofollow")

        assert errors == [], f'Errors have been found while checking if if external links have a tag ' \
                             f'rel="nofollow": {errors}'
