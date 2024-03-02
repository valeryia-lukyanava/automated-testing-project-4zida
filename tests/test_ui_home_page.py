import allure
import pytest

from constants.titles.headers import Headers
from constants.web_elements.tags import Tags
from pom.pages.home_page import HomePage
from constants.titles.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@pytest.mark.chrome_mobile
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
    @allure.title('Check Login via Email')
    def test_login_via_email(self, home_page: HomePage):
        # Login via email is successful
        home_page.visit()
        home_page.login_via_email()

    @allure.id('3')
    @allure.title('Check Search From')
    def test_check_search_form(self, home_page: HomePage):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_tabs_are_working()
        home_page.check_combobox_type()

    @allure.id('4')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        # Footer Links
        home_page.visit()
        home_page.check_footer_links()
