import json
import os

import pytest
from datetime import datetime

from config import UIConfig, PerformanceMeasurementConfig, get_ui_config, UserCredentials
from constants.urls.api_endpoints import APIEndpoints
from pom.models.page import Page
from utils.attach_screenshot import attach_screenshot
from utils.http_requests import send_delete_request
from utils.logger import logger


@pytest.fixture(scope='session')
def url_suffix() -> str:
    yield os.environ["URL_SUFFIX"]


@pytest.fixture(scope='session')
def ui_config() -> UIConfig:
    return UIConfig()


@pytest.fixture(scope='session')
def performance_tests_config() -> PerformanceMeasurementConfig:
    return PerformanceMeasurementConfig()


@pytest.fixture(scope='function')
def new_user_credentials() -> UserCredentials:
    user_credentials = UserCredentials()
    yield user_credentials
    response_code = send_delete_request(f"{APIEndpoints.DELETE_USER}{user_credentials.new_user_email}",
                                        user_credentials.x_api_key)
    if response_code == '404':
        send_delete_request(f"{APIEndpoints.DELETE_USER}{user_credentials.new_user_email}",
                            user_credentials.x_api_key)


@pytest.fixture(scope='session')
def credentials() -> UserCredentials:
    return UserCredentials()


@pytest.fixture(scope='session')
def performance_metrics() -> dict:
    performance_metrics = {}
    yield performance_metrics

    ui_config = get_ui_config()

    if not os.path.exists(ui_config.logging.performance_results_dir):
        os.mkdir(ui_config.logging.performance_results_dir)

    target_output = f'performance-results/metrics_{datetime.now().strftime("%Y-%m-%dT%H%M")}.json'
    with open(target_output, 'a', encoding='utf8') as json_file:
        json.dump(performance_metrics, json_file, indent=6)


@pytest.fixture(scope='function')
def page(request: pytest.FixtureRequest, ui_config: UIConfig) -> Page:
    page_client = Page(ui_config)
    page_client.wait_until_stable()
    yield page_client

    try:
        if ui_config.logging.screenshots_on:
            attach_screenshot(page_client, request.node.name)

        browser_console_logs = [entry for entry in page_client.webdriver.get_log('browser') if entry['level'] != 'INFO']
        if browser_console_logs:
            logger.info(f"Browser console logs: {browser_console_logs}")
    finally:
        page_client.quit()
