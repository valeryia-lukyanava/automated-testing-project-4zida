import allure
import pytest

from constants.navigation_menu import NavigationMenu
from data.navigation_sub_menu import NavigationSubMenu
from pom.pages.home_page import HomePage
from constants.suites import Suite


@pytest.mark.ui
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.UI)
class TestUINavigationMenu:
    @allure.id('1')
    @allure.title('Check Menu "Prodaja" Navigation')
    @pytest.mark.parametrize("index,sub_menu,expected_url", NavigationSubMenu.SUB_MENU_SALE)
    def test_navigation_menu_sale(self, home_page: HomePage, url_suffix: str, index: int, sub_menu: str,
                                  expected_url: str):
        home_page.visit(url_suffix=url_suffix)
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_SALE, sub_menu=sub_menu, expected_url=expected_url)
