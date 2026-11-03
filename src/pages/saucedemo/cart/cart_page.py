
"""
Page Object Model for the SauceDemo Cart page.
"""

from playwright.sync_api import Page, expect

from src.pages.saucedemo.cart.locator.cart_locators import (
    CartLocators,
)


class CartPage:

    def __init__(self, page: Page):
        self.page = page

    def verify_cart_page(self):
        """Verify that the shopping cart page is displayed."""
        expect(
            self.page.locator(CartLocators.PAGE_HEADING)
        ).to_have_text("Your Cart")

    def get_cart_item(self, product_name: str):
        """Find a cart item using its visible product name."""
        product_title = f"Sauce Labs {product_name}"

        return self.page.locator(
            CartLocators.CART_ITEMS
        ).filter(
            has=self.page.get_by_text(
                product_title,
                exact=True,
            )
        )

    def get_item_name(self, product_name: str) -> str:
        """Get the selected item's name from the cart."""
        item = self.get_cart_item(product_name)

        return item.locator(
            CartLocators.ITEM_NAME
        ).inner_text()

    def get_item_price(self, product_name: str) -> str:
        """Get the selected item's price from the cart."""
        item = self.get_cart_item(product_name)

        return item.locator(
            CartLocators.ITEM_PRICE
        ).inner_text()

    def verify_item_in_cart(
        self,
        product_name: str,
        expected_name: str,
        expected_price: str,
    ):
        """Verify the selected item's name and price in the cart."""
        item = self.get_cart_item(product_name)

        expect(
            item.locator(CartLocators.ITEM_NAME)
        ).to_have_text(expected_name)

        expect(
            item.locator(CartLocators.ITEM_PRICE)
        ).to_have_text(expected_price)

    def remove_product(self, product_name: str):
        """Remove a specific product from the cart."""
        item = self.get_cart_item(product_name)

        item.locator(
            CartLocators.REMOVE_BUTTON
        ).click()

    def continue_shopping(self):
        """Return to the Products page."""
        self.page.locator(
            CartLocators.CONTINUE_SHOPPING_BUTTON
        ).click()

    def proceed_to_checkout(self):
        """Click the Checkout button."""
        self.page.locator(
            CartLocators.CHECKOUT_BUTTON
        ).click()

    def get_cart_item_count(self) -> int:
        """Return the number of products currently in the cart."""
        return self.page.locator(
            CartLocators.CART_ITEMS
        ).count()

    def verify_cart_is_empty(self):
        """Verify that no products are displayed in the cart."""
        expect(
            self.page.locator(CartLocators.CART_ITEMS)
        ).to_have_count(0)
