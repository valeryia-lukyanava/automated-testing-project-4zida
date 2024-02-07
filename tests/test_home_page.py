import allure
import pytest

from pom.pages.home_page import HomePage
from constants.titles import Titles
from constants.suites import Suite


@pytest.mark.ui
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.SMOKE)
class TestHomePage:
    @allure.id('1')
    @allure.title('Check the main search pages')
    def test_home_page(self, home_page: HomePage):
        home_page.visit()
        # home_page.check_meta_tag(attribute="content", expected_value="index, follow")
        # home_page.check_link_canonical(attribute="href",
        #                                       expected_value=f"{home_page.page.config.base_url}{endpoint}")
        # home_page.check_logo_is_visible()
        home_page.check_browser_title(expected_title_text=Titles.HOME_PAGE_BROWSER_TITLE)
        home_page.check_search_form_is_visible()
        # home_page.check_search_type(expected_type_name="Stanovi")
        # home_page.check_page_title(expected_title_text=f"Prodaja stanova {city_name}")
        # pytest.assume(home_page.get_title() == "Prodaja stanova Novi Sad - 4zida")
        # pytest.assume(home_page.get_title() == "Prodaja stanova Novi Sad - 4zida")
