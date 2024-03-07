import allure
import pytest
from flaky import flaky

from config import UIConfig, QACredentials
from constants.titles.dropdown_subtypes import DropdownSubtypes
from constants.titles.dropdown_types import DropdownTypes
from constants.titles.headers import Headers
from constants.urls.paths import Paths
from constants.web_elements.tags import Tags
from pom.pages.home_page import HomePage
from constants.titles.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@pytest.mark.chrome_mobile
@pytest.mark.order(1)
@flaky(max_runs=2)
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
    def test_login_via_email(self, home_page: HomePage, credentials_config: QACredentials):
        # TODO: not completed
        home_page.visit()
        home_page.login_via_email(credentials_config.qa_email, credentials_config.qa_password)

    @allure.id('3')
    @allure.title('Check Search Form is visible and Tabs are working')
    def test_check_search_form_is_visible_and_tabs_work(self, home_page: HomePage):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_tabs_are_working()

    @allure.id('4')
    @allure.title('Check Search Form: "Vrsta nekretnine"/”Tip” dropdown')
    def test_check_search_form_type_dropdown(self, home_page: HomePage):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_combobox_type()

    @allure.id('5')
    @allure.title('Check Search Form: Subcategories dropdown')
    @pytest.mark.parametrize("category, subcategory", [
        (DropdownTypes.APARTMENT, DropdownSubtypes.NUMBER_OF_ROOMS),
        (DropdownTypes.HOUSE, DropdownSubtypes.FLOORS),
        (DropdownTypes.OFFICE, DropdownSubtypes.PLACE_TYPE),
        (DropdownTypes.LOT, DropdownSubtypes.LAND_TYPE),
        (DropdownTypes.VEHICLESPOT, DropdownSubtypes.GARAGE_PARKING_TYPE)
    ])
    def test_check_search_form_subcategory_dropdown(self, home_page: HomePage, category: str, subcategory: dict):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.search_form.select_type(category)
        home_page.search_form.check_combobox_subtype(category,
                                                     list(subcategory.keys())[0],
                                                     list(subcategory.values())[0])

    @allure.id('6')
    @allure.title('Check Search Form Inputs "Cena do" and "m2 od"')
    @pytest.mark.parametrize("property_type,price_to,m2_from,expected_path", [
        (DropdownTypes.HOUSE, "0", "0", ""),
        (DropdownTypes.HOUSE, "100000", "50", f"{Paths.SALE_HOUSES}?jeftinije_od=100000eur&vece_od=50m2"),
        (DropdownTypes.HOUSE, "-100000", "50", ""),
        (DropdownTypes.HOUSE, "100000", "-50", "")
    ])
    def test_check_search_form_inputs(self, home_page: HomePage, property_type: str, price_to: str, m2_from: str,
                                      expected_path: str):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.search_with_parameters(property_type=property_type, price_to=price_to, m2_from=m2_from)
        home_page.check_the_search_returns_no_server_error(expected_path)

    @allure.id('7')
    @allure.title('Check "Popularni gradovi" Quick Links')
    def test_place_suggestions_quick_links(self, home_page: HomePage):
        home_page.visit()
        home_page.check_place_suggestions()

    @allure.id('8')
    @allure.title('Check "Service offerings" Carousel')
    def test_carousel_added_values(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_service_offerings()

    @allure.id('9')
    @allure.title('Check "Istaknute Agencije" Carousel')
    def test_carousel_branding_agencies(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_branding_agencies()

    @allure.id('10')
    @allure.title('Check "Premijum oglasi" Carousel')
    def test_carousel_premium_ads(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_premium_ads()

    @allure.id('11')
    @allure.title('Check "Najnoviji blog postovi" Widget')
    def test_blog_post_widget(self, home_page: HomePage):
        home_page.visit()
        home_page.check_blog_post_widget()

    @allure.id('12')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        # Footer Links
        home_page.visit()
        home_page.check_footer_links()
