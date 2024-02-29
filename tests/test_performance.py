import allure
import pytest
from flaky import flaky

from config import UIConfig, PerformanceMeasurementConfig
from pom.models.page import Page
from pom.pages.home_page import HomePage
from constants.suites import Suite
from utils.attach_screenshot import attach_screenshot
from utils.calculate_median_values import get_median_values_for_metrics


@pytest.mark.ui
@pytest.mark.performance
@allure.severity(allure.severity_level.CRITICAL)
@allure.suite(Suite.PERFORMANCE)
@flaky(max_runs=2)
class TestPerformance:
    @allure.id('1')
    @allure.title('Performance tests for Home page')
    def test_home_page_performance(self,
                                   performance_tests_config: PerformanceMeasurementConfig(),
                                   performance_metrics: dict):
        ui_config = UIConfig()

        for n in range(performance_tests_config.number_of_measurements):
            page_client = Page(ui_config)
            page_client.wait_until_stable()
            home_page = HomePage(page_client)
            home_page.get_performance_metrics(run=n + 1, performance_metrics=performance_metrics)

            if ui_config.logging.screenshots_on:
                attach_screenshot(page_client, f"test_home_page_performance_measurement_{n + 1}")

            page_client.quit()

        with allure.step(f"Comparing the median values with expected values of performance metrics"):
            median_values = get_median_values_for_metrics(performance_metrics, ui_config)
            actual_lcp = median_values["LCP"]
            actual_ttfb = median_values["TTFB"]
            expected_lcp = performance_tests_config.lcp
            expected_ttfb = performance_tests_config.ttfb

            description = f"Expected: LCP is under {expected_lcp} ms and TTFB is under {expected_ttfb} ms. " \
                          f"Actual: LCP = {actual_lcp} ms and TTFB = {actual_ttfb} ms"

            with allure.step(description):
                assert actual_lcp < expected_lcp and actual_ttfb < expected_ttfb, \
                    f"Performance metrics do not meet the requirements. {description}"
