import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from locators.login_form_locators import LoginFormLocators
from pom.page_factory.button import Button
from pom.page_factory.component import Component
from pom.page_factory.input import Input
from pom.pages.base_page import BasePage
from pom.models.page import Page
from pom.pages.google_sign_in_page import GoogleSignInPage
from utils.logger import logger
from selenium.webdriver.support import expected_conditions as EC


class LoginForm(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.login_dialog = Component(
            page, locator=LoginFormLocators.LOGIN_DIALOG, name="Login Dialog"
        )
        self.login_google_iframe = Component(
            page, locator=LoginFormLocators.LOGIN_GOOGLE_IFRAME, name="Login Google iframe"
        )
        self.login_google_button = Button(
            page, locator=LoginFormLocators.LOGIN_GOOGLE_BUTTON, name="Google button"
        )
        self.login_via_email_button = Button(
            page, locator=LoginFormLocators.LOGIN_VIA_EMAIL_BUTTON, name="Button 'Nastavi sa email adresom'"
        )
        self.login_email_input = Input(
            page, locator=LoginFormLocators.LOGIN_EMAIL_INPUT, name="Input 'Email'"
        )
        self.login_password_input = Input(
            page, locator=LoginFormLocators.LOGIN_PASSWORD_INPUT, name="Input 'Lozinka'"
        )
        self.password_input = Input(
            page, locator=LoginFormLocators.PASSWORD_INPUT, name="Input 'Lozinka'"
        )
        self.login_confirm_password_input = Input(
            page, locator=LoginFormLocators.CONFIRM_PASSWORD_INPUT, name="Input 'Potvrdi lozinku'"
        )
        self.first_name_input = Input(
            page, locator=LoginFormLocators.FIRST_NAME_INPUT, name="Input 'Ime'"
        )
        self.login_submit_button = Button(
            page, locator=LoginFormLocators.LOGIN_SUBMIT_BUTTON, name="Button 'Prijavi se'"
        )
        self.register_section = Component(
            page, locator=LoginFormLocators.REGISTER_SECTION, name="Section 'Nemaš nalog? Napravi ga:'"
        )
        self.register_form = Component(
            page, locator=LoginFormLocators.REGISTER_FORM, name="Form 'Nemaš nalog? Napravi ga:'"
        )
        self.register_new_user_button = Button(
            page, locator=LoginFormLocators.REGISTER_NEW_USER_BUTTON, name="Button 'Registruj se'"
        )
        self.continue_with_email_button = Button(
            page, locator=LoginFormLocators.CONTINUE_WITH_EMAIL, name="Button 'Nastavi sa email adresom'"
        )
        self.user_agreement_checkbox = Button(
            page, locator=LoginFormLocators.USER_AGREEMENT_CHECKBOX,
            name="Checkbox 'Prihvatam Obaveštenje o privatnosti, ...'"
        )
        self.register_submit_button = Button(
            page, locator=LoginFormLocators.REGISTER_SUBMIT_BUTTON, name="Button 'Registruj se'"
        )

    @allure.step('Login via Email')
    def login_via_email(self, email: str, password: str):
        time.sleep(1)
        self.login_via_email_button.should_be_visible()
        self.login_via_email_button.click()
        time.sleep(1)
        self.login_email_input.should_be_visible()
        self.login_email_input.fill(email)
        self.login_password_input.should_be_visible()
        self.login_password_input.fill(password)
        self.login_submit_button.should_be_visible()
        self.login_submit_button.click()

    @allure.step('Login via Google')
    def login_via_google(self, email, password):
        time.sleep(2)
        self.login_google_iframe.should_be_visible()
        WebDriverWait(self.page.webdriver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, LoginFormLocators.LOGIN_GOOGLE_IFRAME)))
        # self.page.webdriver.switch_to.frame(0)
        logger.info(f"Page Source: {self.page.webdriver.page_source}")
        WebDriverWait(self.page.webdriver, 10).until(
            EC.element_to_be_clickable((By.XPATH, LoginFormLocators.LOGIN_GOOGLE_BUTTON)))
        logger.info(f"Page Source: {self.page.webdriver.page_source}")
        # self.page.get_xpath_and_check_visibility(LoginFormLocators.LOGIN_GOOGLE_BUTTON)
        self.page.click_with_js(LoginFormLocators.LOGIN_GOOGLE_BUTTON)
        original_window = self.page.get_original_window_handle()
        self.page.switch_to_new_window()
        google_sign_in_page = GoogleSignInPage(self.page)
        google_sign_in_page.sign_in_google_account(email, password)
        self.page.webdriver.switch_to.window(original_window)

    @allure.step('Register a New User')
    def register_new_user(self, email, password, first_name):
        time.sleep(2)
        self.register_new_user_button.should_be_visible()
        self.register_new_user_button.click()
        self.register_section.should_be_visible()
        self.continue_with_email_button.should_be_visible()
        self.continue_with_email_button.click()

        self.register_form.should_be_visible()
        self.login_email_input.should_be_visible()
        self.login_email_input.fill(email)
        self.password_input.should_be_visible()
        self.password_input.fill(password)
        self.login_confirm_password_input.should_be_visible()
        self.login_confirm_password_input.fill(password)
        self.first_name_input.should_be_visible()
        self.first_name_input.fill(first_name)
        self.user_agreement_checkbox.should_be_visible()
        self.user_agreement_checkbox.click()
        self.register_submit_button.should_be_visible()
        self.register_submit_button.click()
