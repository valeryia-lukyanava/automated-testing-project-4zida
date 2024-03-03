import allure
import pytest

from constants.titles.dropdown_type import DropdownType
from constants.titles.headers import Headers
from constants.urls.routes import UIRoutes
from constants.web_elements.tags import Tags
from pom.pages.home_page import HomePage
from constants.titles.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@pytest.mark.chrome_mobile
@pytest.mark.order(1)
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
        # TODO: not completed
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
    @allure.sub_suite('Search Form Inputs "Cena do" and "m2 od"')
    @allure.title('Check Search Form Inputs "Cena do" and "m2 od"')
    @pytest.mark.parametrize("property_type,price_to,m2_from,expected_path", [
        (DropdownType.HOUSE, "0", "0", UIRoutes.SALE_HOUSES),
        (DropdownType.HOUSE, "100000", "50", UIRoutes.SALE_HOUSES),
        (DropdownType.HOUSE, "-100000", "50", UIRoutes.SALE_HOUSES),
        (DropdownType.HOUSE, "100000", "-50", UIRoutes.SALE_HOUSES)
    ])
    def test_check_search_form_inputs(self, home_page: HomePage, property_type: str, price_to: str, m2_from: str,
                                      expected_path: str):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.search_with_parameters(property_type=property_type, price_to=price_to, m2_from=m2_from)
        home_page.check_the_search_returns_no_error(path=expected_path)

    @allure.id('5')
    @allure.title('Check "Popularni gradovi" Quick Links')
    def test_place_suggestions_quick_links(self, home_page: HomePage):
        home_page.visit()
        home_page.check_place_suggestions()

    @allure.id('6')
    @allure.title('Check "Service offerings" Carousel')
    def test_carousel_added_values(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_service_offerings()

    @allure.id('7')
    @allure.title('Check "Istaknute Agencije" Carousel')
    def test_carousel_branding_agencies(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_branding_agencies()

    @allure.id('8')
    @allure.title('Check "Premijum oglasi" Carousel')
    def test_carousel_premium_ads(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_premium_ads()

    @allure.id('9')
    @allure.title('Check "Najnoviji blog postovi" Widget')
    def test_blog_post_widget(self, home_page: HomePage):
        home_page.visit()
        home_page.check_blog_post_widget()

    @allure.id('10')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        # Footer Links
        home_page.visit()
        home_page.check_footer_links()
