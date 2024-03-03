import allure
import pytest
from flaky import flaky

from constants.titles.navigation_menu import NavigationMenu
from constants.urls.navigation_sub_menu import NavigationSubMenu
from pom.pages.home_page import HomePage
from constants.suites import Suite


@pytest.mark.ui
@pytest.mark.chrome_mobile
@pytest.mark.order(2)
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.UI)
class TestUINavigationMenu:
    @allure.id('1')
    @allure.sub_suite('Menu Navigation: "Prodaja"')
    @allure.title('Check Menu Navigation: "Prodaja"')
    @pytest.mark.parametrize("index,sub_menu,expected_url", NavigationSubMenu.SUB_MENU_SALE)
    def test_navigation_menu_sale(self, home_page: HomePage, index: int, sub_menu: str, expected_url: str):
        home_page.visit()
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_SALE, sub_menu=sub_menu, expected_url=expected_url)

    @allure.id('2')
    @allure.sub_suite('Menu Navigation: "Izdavanje"')
    @allure.title('Check Menu Navigation: "Izdavanje"')
    @pytest.mark.parametrize("index,sub_menu,expected_url", NavigationSubMenu.SUB_MENU_RENT)
    def test_navigation_menu_rent(self, home_page: HomePage, index: int, sub_menu: str, expected_url: str):
        home_page.visit()
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_RENT, sub_menu=sub_menu, expected_url=expected_url)

    @allure.id('3')
    @allure.sub_suite('Menu Navigation: "Novogradnja"')
    @allure.title('Check Menu Navigation: "Novogradnja"')
    @pytest.mark.parametrize("index,sub_menu,expected_url", NavigationSubMenu.SUB_MENU_NEW)
    def test_navigation_menu_new(self, home_page: HomePage, index: int, sub_menu: str, expected_url: str):
        home_page.visit()
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_NEW, sub_menu=sub_menu, expected_url=expected_url)

    @allure.id('4')
    @allure.sub_suite('Menu Navigation: "Oglašavanje"')
    @allure.title('Check Menu Navigation: "Oglašavanje"')
    @pytest.mark.parametrize("index,sub_menu,expected_url", NavigationSubMenu.SUB_MENU_ADVERTISEMENT)
    def test_navigation_menu_advertisement(self, home_page: HomePage, index: int, sub_menu: str, expected_url: str):
        home_page.visit()
        home_page.check_menu_navigation(menu=NavigationMenu.MENU_ADVERTISEMENT, sub_menu=sub_menu,
                                        expected_url=expected_url)
