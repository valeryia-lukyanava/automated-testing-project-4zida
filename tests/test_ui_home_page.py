import allure
import pytest
from flaky import flaky

from config import QACredentials
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
        home_page.visit()
        home_page.check_browser_title(expected_title_text=Titles.HOME_PAGE_BROWSER_TITLE)
        home_page.check_page_headers(header_tag=Tags.H1, expected_values=Headers.H1)
        home_page.check_search_form_is_visible()

    @allure.id('2')
    @allure.title('Cookie Policy Notification is Visible and Links are Clickable')
    def test_cookie_policy_notification(self, home_page: HomePage):
        home_page.visit(cookie_enabled=True)
        home_page.check_search_form_is_visible()

    @allure.id('3')
    @allure.title('Check Login via Google')
    def test_login_via_google(self, home_page: HomePage, credentials: QACredentials):
        home_page.visit()
        home_page.login_click()
        home_page.login_via_google(email=credentials.google_qa_email, password=credentials.google_qa_password)

    @allure.id('4')
    @allure.title('Check Login via Email')
    def test_login_via_email(self, home_page: HomePage, credentials: QACredentials):
        home_page.visit()
        home_page.login_click()
        home_page.login_via_email(email=credentials.qa_email, password=credentials.qa_password)

    @allure.id('5')
    @allure.title('Check Search Form is visible and Tabs are working')
    def test_check_search_form_is_visible_and_tabs_work(self, home_page: HomePage):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_tabs_are_working()

    @allure.id('6')
    @allure.title('Check Search Form: "Vrsta nekretnine"/”Tip” dropdown')
    def test_check_search_form_type_dropdown(self, home_page: HomePage):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_combobox_type()

    @allure.id('7')
    @allure.title('Check Search Form: Subcategories dropdown')
    @pytest.mark.parametrize("category, subcategory", [
        (DropdownTypes.APARTMENT, DropdownSubtypes.NUMBER_OF_ROOMS),
        (DropdownTypes.HOUSE, DropdownSubtypes.FLOORS),
        (DropdownTypes.OFFICE, DropdownSubtypes.PLACE_TYPE),
        (DropdownTypes.LAND, DropdownSubtypes.LAND_TYPE),
        (DropdownTypes.GARAGE, DropdownSubtypes.GARAGE_PARKING_TYPE)
    ])
    def test_check_search_form_subcategory_dropdown(self, home_page: HomePage, category: str, subcategory: dict):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.search_form.select_type(category)
        home_page.search_form.check_combobox_subtype(type_value=category,
                                                     subtype=list(subcategory.keys())[0],
                                                     subtype_values=list(subcategory.values())[0])

    @allure.id('8')
    @allure.title('Check "Upiši lokaciju" Autocomplete Multiselect')
    @pytest.mark.parametrize("input_values,locations,category,expected_path", [
        (["Beo"], ["Beograd"],
         DropdownTypes.HOUSE, f"{Paths.SALE_HOUSES}/beograd"),
        (["Subotica"], ["Subotica (Gradske lokacije)"],
         DropdownTypes.OFFICE, f"{Paths.SALE_OFFICES}/gradske-lokacije-subotica"),
        (["novi sad"], ["Novi Sad (Gradske i okolne lokacije)"],
         DropdownTypes.OFFICE, f"{Paths.SALE_OFFICES}/novi-sad"),
        (["Beograd", "Subotica", "Novi Sad"], ["Beograd", "Subotica (Gradske lokacije)", "Novi Sad (Gradske lokacije)"],
         DropdownTypes.HOUSE,
         f"{Paths.SALE_HOUSES}/beograd?mesto=gradske-lokacije-subotica&mesto=gradske-lokacije-novi-sad"),
    ])
    def test_location_multiselect(self, home_page: HomePage, input_values: list, locations: list, category: str,
                                  expected_path: str):
        home_page.visit()
        home_page.check_location_multiselect(input_values=input_values, locations=locations, category=category,
                                             expected_path=expected_path)

    @allure.id('9')
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

    @allure.id('10')
    @pytest.mark.parametrize("category,subcategory,checkbox_is_available,expected_url", [
        (DropdownTypes.APARTMENT, "Troiposoban stan", True, f"{Paths.SALE_APARTMENTS}?struktura=troiposoban"),
        (DropdownTypes.HOUSE, None, False, Paths.SALE_HOUSES),
        (DropdownTypes.OFFICE, None, True, f"{Paths.NEW_BUILDINGS}/prodaja-poslovnih-prostora"),
        (DropdownTypes.LAND, None, False, Paths.SALE_LANDS),
        (DropdownTypes.GARAGE, None, True, f"{Paths.NEW_BUILDINGS}{Paths.SALE_GARAGE}")
    ])
    @allure.title('Check "Samo novogradnja" checkbox')
    def test_check_checkbox_new_buildings_only(self, home_page: HomePage, category: str, subcategory: str,
                                               checkbox_is_available: bool, expected_url: str):
        home_page.visit()
        home_page.check_search_form_is_visible()
        home_page.check_checkbox_new_buildings_only(category=category, subcategory=subcategory,
                                                    checkbox_is_available=checkbox_is_available,
                                                    expected_url=expected_url)

    # "Stan na dan" checkbox

    @allure.id('11')
    @allure.title('Check "Popularni gradovi" Quick Links')
    def test_place_suggestions_quick_links(self, home_page: HomePage):
        home_page.visit()
        home_page.check_place_suggestions()

    @allure.id('12')
    @allure.title('Check "Service offerings" Carousel')
    def test_carousel_added_values(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_service_offerings()

    @allure.id('13')
    @allure.title('Check "Istaknute Agencije" Carousel')
    def test_carousel_branding_agencies(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_branding_agencies()

    @allure.id('14')
    @allure.title('Check "Premijum oglasi" Carousel')
    def test_carousel_premium_ads(self, home_page: HomePage):
        home_page.visit()
        home_page.check_carousel_premium_ads()

    @allure.id('15')
    @allure.title('Check "Najnoviji blog postovi" Widget')
    def test_blog_post_widget(self, home_page: HomePage):
        home_page.visit()
        home_page.check_blog_post_widget()

    @allure.id('16')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        home_page.visit()
        home_page.check_footer_links()
