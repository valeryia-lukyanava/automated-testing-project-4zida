import allure

from locators.home_page_locators import HomePageLocators
from pom.components.cookies_modal import CookiesModal
from pom.models.page import Page


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.errors = []
        self.cookies_modal = CookiesModal(page)

    def visit(self, url: str = '', url_suffix: str = '') -> None:
        # with allure.step(f'Opening the url "{self.page.config.base_url}{url}" and close cookies'):
        with allure.step(f'Opening the url "{self.page.config.base_url}{url}"'):
            self.page.get(url, url_suffix)
            # self.cookies_modal.close() # TODO : remove for next env ?

    def get_performance_metrics(self, run: int, performance_metrics: dict, url: str = '') -> None:
        with allure.step(f'Performance test run №{run}'):
            with allure.step(f'Opening the url "{self.page.config.base_url}{url}"'):
                self.page.get(url)

            self.page.check_web_element_located(HomePageLocators.LOGO)

            with allure.step(f'Measuring performance metrics: '
                             f'TTFB, LCP, Page Load Time, End-to-End Response Time"'):
                self.page.get_performance_metrics(run, performance_metrics)

    def reload(self) -> Page:
        page_url = self.page.url()
        with allure.step(f'Reloading page with url "{self.page.config.base_url}{page_url}"'):
            return self.page.reload()
