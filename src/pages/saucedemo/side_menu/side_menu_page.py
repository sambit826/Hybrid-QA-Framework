
"""
Page Object Model for the SauceDemo Side Menu.
"""

from playwright.sync_api import Page, expect

from src.pages.saucedemo.side_menu.locator.side_menu_locators import (
    SideMenuLocators,
)

from src.pages.saucedemo.login.locator.login_locators import (
    LoginLocators,
)


class SideMenuPage:

    def __init__(self, page: Page):
        self.page = page

    def open_menu(self):
        """Open the side menu."""
        self.page.locator(
            SideMenuLocators.MENU_BUTTON
        ).click()

    def verify_menu_is_open(self):
        """Verify that the main menu options are visible."""
        expect(
            self.page.locator(
                SideMenuLocators.DYNAMIC_CATALOG_LINK
            )
        ).to_be_visible()

        expect(
            self.page.locator(
                SideMenuLocators.LOGOUT_LINK
            )
        ).to_be_visible()

    def open_dynamic_catalog(self):
        """Expand the Dynamic Catalog menu."""
        self.page.locator(
            SideMenuLocators.DYNAMIC_CATALOG_LINK
        ).click()

    def verify_dynamic_catalog_options(self):
        """Verify Lazy Load and Spinner options are visible."""
        expect(
            self.page.locator(
                SideMenuLocators.LAZY_LOAD_LINK
            )
        ).to_be_visible()

        expect(
            self.page.locator(
                SideMenuLocators.SPINNER_LINK
            )
        ).to_be_visible()

    def open_lazy_load(self):
        """Open the Lazy Load page."""
        self.page.locator(
            SideMenuLocators.LAZY_LOAD_LINK
        ).click()

    def open_spinner(self):
        """Open the Spinner page."""
        self.page.locator(
            SideMenuLocators.SPINNER_LINK
        ).click()

    def logout(self):
        """Log out from SauceDemo."""
        self.page.locator(
            SideMenuLocators.LOGOUT_LINK
        ).click()

    def verify_logout(self):
        """Verify that the user is back on the login page."""
        expect(
            self.page.locator(
                LoginLocators.LOGIN_BUTTON
            )
        ).to_be_visible()
