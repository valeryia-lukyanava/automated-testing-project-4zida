import os
from datetime import datetime

import allure

from config import get_ui_config
from pom.models.page import Page


def attach_screenshot(page: Page, test_name: str):
    ui_config = get_ui_config()

    if not os.path.exists(ui_config.logging.screenshots_dir):
        os.mkdir(ui_config.logging.screenshots_dir)

    if "[" in test_name:
        test_name = test_name.split("-")[0] + "]"

    screenshot = page.screenshot(f'screenshots/{test_name}{datetime.now().strftime("%Y-%m-%dT%H%M%S")}.png')

    allure.attach.file(
        screenshot, name=f'{test_name}', attachment_type=allure.attachment_type.PNG
    )
