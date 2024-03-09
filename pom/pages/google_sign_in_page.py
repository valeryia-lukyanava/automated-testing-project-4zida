import time

import allure
from locators.google_sign_in_page import GoogleSignInPageLocators
from pom.page_factory.button import Button
from pom.page_factory.input import Input
from pom.pages.base_page import BasePage
from pom.models.page import Page


class GoogleSignInPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.email_input = Input(
            page, locator=GoogleSignInPageLocators.EMAIL_INPUT, name='Input "Email"'
        )
        self.password_input = Input(
            page, locator=GoogleSignInPageLocators.PASSWORD_INPUT, name='Input "Password"'
        )
        self.next_button = Button(
            page, locator=GoogleSignInPageLocators.NEXT_BUTTON, name='Button "Next"'
        )
        self.confirm_button = Button(
            page, locator=GoogleSignInPageLocators.CONFIRM_BUTTON, name='Button "Confirm"'
        )

    @allure.step('Sign In Google Account')
    def sign_in_google_account(self, email: str, password: str):
        self.email_input.should_be_visible()
        self.email_input.fill(email)
        self.next_button.should_be_visible()
        self.next_button.click()
        self.password_input.should_be_visible()
        self.password_input.fill(password)
        self.next_button.should_be_visible()
        self.next_button.click()
