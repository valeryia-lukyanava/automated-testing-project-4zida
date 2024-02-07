import allure
from selenium.common.exceptions import TimeoutException

from pom.page_factory.button import Button
from utils.logger import logger
from pom.models.page import Page


class CookiesModal:
    def __init__(self, page: Page) -> None:
        self.close_button = Button(
            page,
            locator='//app-cookie-consent//button',
            name='Close it'
        )
        self.find_out_more_button = Button(
            page,
            locator='//app-cookie-consent//a',
            name='Find out more'
        )

    @allure.step('Accepting all cookies')
    def close(self):
        try:
            if self.close_button.is_displayed() and self.find_out_more_button.is_displayed():
                self.close_button.click()
        except TimeoutException:
            logger.error('Cookies modal did not appear')
