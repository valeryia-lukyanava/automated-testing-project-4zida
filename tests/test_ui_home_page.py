import allure
import pytest

from constants.headers import Headers
from constants.tags import Tags
from pom.pages.home_page import HomePage
from constants.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.UI)
class TestUIHomePage:
    @allure.id('1')
    @allure.title('Check the Home page is loading')
    def test_home_page(self, home_page: HomePage):
        # Page next.4zida.rs is loading
        home_page.visit()
        home_page.check_browser_title(expected_title_text=Titles.HOME_PAGE_BROWSER_TITLE)
        home_page.check_page_headers(header_tag=Tags.H1, expected_values=Headers.H1)
        home_page.check_search_form_is_visible()

    @allure.id('2')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        # Footer Links
        home_page.visit()
        home_page.check_footer_links()
