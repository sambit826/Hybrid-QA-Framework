
"""
Page Object Model for the SauceDemo Products page.
"""

from playwright.sync_api import Page, expect

from src.pages.saucedemo.products.locator.products_locators import (
    ProductsLocators,
)


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

    def is_products_page(self) -> bool:
        """Check whether the Products page is currently displayed."""
        heading = self.page.locator(
            ProductsLocators.PAGE_HEADING
        )

        return (
            heading.is_visible()
            and heading.inner_text().strip() == "Products"
        )

    def verify_products_page(self):
        """Verify that the Products page is displayed."""
        expect(
            self.page.locator(ProductsLocators.PAGE_HEADING)
        ).to_have_text("Products")

    def get_product_card(self, product_name: str):
        """Find a product card using its visible product name."""
        product_title = f"Sauce Labs {product_name}"

        return self.page.locator(
            ProductsLocators.PRODUCT_CARDS
        ).filter(
            has=self.page.get_by_text(
                product_title,
                exact=True,
            )
        )

    def get_product_name(self, product_name: str) -> str:
        """Get the displayed name of a selected product."""
        product_card = self.get_product_card(product_name)

        return product_card.locator(
            ProductsLocators.PRODUCT_NAME
        ).inner_text()

    def get_product_price(self, product_name: str) -> str:
        """Get the displayed price of a selected product."""
        product_card = self.get_product_card(product_name)

        return product_card.locator(
            ProductsLocators.PRODUCT_PRICE
        ).inner_text()

    def get_all_product_names(self) -> list:
        """Return all displayed product names in their current order."""
        return self.page.locator(
            ProductsLocators.PRODUCT_NAME
        ).all_inner_texts()

    def get_all_product_prices(self) -> list:
        """Return all displayed product prices in their current order."""
        return self.page.locator(
            ProductsLocators.PRODUCT_PRICE
        ).all_inner_texts()

    def add_product_to_cart(self, product_name: str):
        """Add a product to the cart using its visible name."""
        product_card = self.get_product_card(product_name)

        product_card.get_by_role(
            "button",
            name="Add to cart",
        ).click()

    def sort_products(self, sort_option: str):
        """Sort products using the supplied sorting option."""
        self.page.locator(
            ProductsLocators.SORT_DROPDOWN
        ).select_option(sort_option)

    def open_cart(self):
        """Open the shopping cart."""
        self.page.locator(
            ProductsLocators.CART_LINK
        ).click()

    def get_cart_item_count(self) -> int:
        """Return the number of items shown in the cart badge."""
        badge = self.page.locator(
            ProductsLocators.CART_BADGE
        )

        if badge.count() == 0:
            return 0

        return int(badge.inner_text())
