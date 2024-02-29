import allure
import pytest
from flaky import flaky

from constants.headers import Headers
from constants.navigation_menu import NavigationMenu
from constants.navigation_sub_menu import NavigationSubMenu
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
        # 1. Page next.4zida.rs is loading
        home_page.visit()
        home_page.check_browser_title(expected_title_text=Titles.HOME_PAGE_BROWSER_TITLE)
        home_page.check_page_headers(header_tag=Tags.H1, expected_values=Headers.H1)

        # 2. Search form - NOT READY
        home_page.check_search_form_is_visible()

        # 3. Quick Links "Quick Links" - NOT READY

        # 4. Carousel Added Values - ?

        # 5. Carousel "Istaknute Agencije" - NOT READY

        # 6. Carousel "Premijum oglasi" - ?

        # 7. "Najnoviji blog postovi" Widget - ?

        # home_page.check_meta_tag(attribute="content", expected_value="index, follow")
        # home_page.check_link_canonical(attribute="href",
        #                                       expected_value=f"{home_page.page.config.base_url}{endpoint}")
        # home_page.check_logo_is_visible()
        # home_page.check_search_type(expected_type_name="Stanovi")
        # home_page.check_page_headers(expected_title_text=f"Prodaja stanova {city_name}")
        # pytest.assume(home_page.get_title() == "Prodaja stanova Novi Sad - 4zida")
        # pytest.assume(home_page.get_title() == "Prodaja stanova Novi Sad - 4zida")

    @allure.id('3')
    @allure.title('Check Menu "Prodaja" Navigation')
    @pytest.mark.parametrize("number, sub_menu,expected_url", NavigationSubMenu.SUB_MENU_SALE)
    def test_navigation_menu_sale(self, home_page: HomePage, number: int, sub_menu: str, expected_url: str):
        home_page.visit()
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_SALE, sub_menu=sub_menu, expected_url=expected_url)

    @allure.id('4')
    @allure.title('Check Footer Links')
    def test_footer_links(self, home_page: HomePage):
        # 8. Footer Links
        home_page.visit()
        home_page.check_footer_links()
