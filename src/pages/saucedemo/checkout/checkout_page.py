
"""
Page Object Model for the SauceDemo Checkout process.
"""

from playwright.sync_api import Page, expect

from src.pages.saucedemo.checkout.locator.checkout_locators import (
    CheckoutLocators,
)


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

    def enter_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ):
        """Enter customer information on the checkout page."""
        self.page.locator(
            CheckoutLocators.FIRST_NAME_INPUT
        ).fill(first_name)

        self.page.locator(
            CheckoutLocators.LAST_NAME_INPUT
        ).fill(last_name)

        self.page.locator(
            CheckoutLocators.POSTAL_CODE_INPUT
        ).fill(postal_code)

    def continue_to_overview(self):
        """Continue from checkout information to order overview."""
        self.page.locator(
            CheckoutLocators.CONTINUE_BUTTON
        ).click()

    def finish_order(self):
        """Finish and submit the order."""
        self.page.locator(
            CheckoutLocators.FINISH_BUTTON
        ).click()

    def verify_order_confirmation(
        self,
        expected_heading: str,
        expected_message: str,
    ):
        """Verify the order confirmation heading and message."""
        expect(
            self.page.locator(
                CheckoutLocators.CONFIRMATION_HEADING
            )
        ).to_have_text(expected_heading)

        expect(
            self.page.locator(
                CheckoutLocators.CONFIRMATION_MESSAGE
            )
        ).to_have_text(expected_message)

    def get_confirmation_heading(self) -> str:
        """Return the order confirmation heading."""
        return self.page.locator(
            CheckoutLocators.CONFIRMATION_HEADING
        ).inner_text()

    def get_confirmation_message(self) -> str:
        """Return the order confirmation message."""
        return self.page.locator(
            CheckoutLocators.CONFIRMATION_MESSAGE
        ).inner_text()

    def back_to_products(self):
        """Return to the Products page after order completion."""
        self.page.locator(
            CheckoutLocators.BACK_HOME_BUTTON
        ).click()
