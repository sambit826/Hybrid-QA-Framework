
"""
Product test cases for SauceDemo.
"""

from decimal import Decimal

import pytest

from setup_blocks.constants import (
    load_product_configurations,
    SORT_OPTIONS,
)


def make_product_test_id(product):
    """Generate readable test IDs from product configuration."""
    return (
        f"product_{product['number']}_"
        f"{product['product_name'].lower().replace(' ', '_')}"
    )


def test_products_page_displayed(authenticated_page, products_page):
    """Verify that a valid login displays the Products page."""

    products_page.verify_products_page()

    print("\nProducts page displayed successfully.")


@pytest.mark.parametrize(
    "product",
    load_product_configurations(),
    ids=make_product_test_id,
)
def test_add_product_to_cart(
    product,
    authenticated_page,
    products_page,
):
    """Verify that a configured product can be added to the cart."""

    product_name = product["product_name"]

    products_page.add_product_to_cart(product_name)

    assert products_page.get_cart_item_count() == 1

    print(f"\nProduct added successfully: {product_name}")


def test_sort_products_price_low_to_high(
    authenticated_page,
    products_page,
):
    """Verify that products can be sorted by ascending price."""

    products_page.sort_products(
        SORT_OPTIONS["PRICE_LOW_TO_HIGH"]
    )

    displayed_prices = products_page.get_all_product_prices()

    actual_prices = [
        Decimal(price.replace("$", ""))
        for price in displayed_prices
    ]

    assert actual_prices == sorted(actual_prices)

    print("\nProducts sorted by price: low to high.")


def test_sort_products_price_high_to_low(
    authenticated_page,
    products_page,
):
    """Verify that products can be sorted by descending price."""

    products_page.sort_products(
        SORT_OPTIONS["PRICE_HIGH_TO_LOW"]
    )

    displayed_prices = products_page.get_all_product_prices()

    actual_prices = [
        Decimal(price.replace("$", ""))
        for price in displayed_prices
    ]

    assert actual_prices == sorted(
        actual_prices,
        reverse=True,
    )

    print("\nProducts sorted by price: high to low.")
