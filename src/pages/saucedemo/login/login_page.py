
"""
Page Object Model for the SauceDemo Login page.
"""

from playwright.sync_api import Page, expect

from src.pages.saucedemo.login.locator.login_locators import LoginLocators


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, base_url: str):
        """Open the SauceDemo login page."""
        self.page.goto(base_url)

    def enter_username(self, username: str):
        """Enter username."""
        self.page.locator(LoginLocators.USERNAME_INPUT).fill(username)

    def enter_password(self, password: str):
        """Enter password."""
        self.page.locator(LoginLocators.PASSWORD_INPUT).fill(password)

    def click_login(self):
        """Click the Login button."""
        self.page.locator(LoginLocators.LOGIN_BUTTON).click()

    def login(self, username: str, password: str):
        """Perform the complete login action."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def verify_login_error(self, expected_message: str):
        """Verify the login error message."""
        expect(
            self.page.locator(LoginLocators.ERROR_MESSAGE)
        ).to_have_text(expected_message)

    def close_login_error(self):
        """Close the login error message."""
        self.page.locator(LoginLocators.ERROR_CLOSE_BUTTON).click()
