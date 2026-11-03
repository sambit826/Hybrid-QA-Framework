
"""
Cart test cases for SauceDemo.
"""

import pytest

from setup_blocks.constants import load_product_configurations


def make_product_test_id(product):
    """Generate readable test IDs from product configuration."""
    return (
        f"product_{product['number']}_"
        f"{product['product_name'].lower().replace(' ', '_')}"
    )


@pytest.mark.parametrize(
    "product",
    load_product_configurations(),
    ids=make_product_test_id,
)
def test_verify_product_details_in_cart(
    product,
    authenticated_page,
    products_page,
    cart_page,
):
    """
    Verify that the product name and price in the cart
    match the details displayed on the Products page.
    """

    product_name = product["product_name"]

    # Capture product details before adding to cart.
    expected_name = products_page.get_product_name(product_name)
    expected_price = products_page.get_product_price(product_name)

    # Add the product to the cart.
    products_page.add_product_to_cart(product_name)

    # Open and verify the cart.
    products_page.open_cart()
    cart_page.verify_cart_page()

    # Compare the captured product details with cart details.
    cart_page.verify_item_in_cart(
        product_name,
        expected_name,
        expected_price,
    )

    print(
        f"\nCart details verified: "
        f"{expected_name} - {expected_price}"
    )


@pytest.mark.parametrize(
    "product",
    load_product_configurations(),
    ids=make_product_test_id,
)
def test_remove_product_from_cart(
    product,
    authenticated_page,
    products_page,
    cart_page,
):
    """Verify that a product can be removed from the cart."""

    product_name = product["product_name"]

    products_page.add_product_to_cart(product_name)
    products_page.open_cart()

    cart_page.verify_cart_page()
    cart_page.remove_product(product_name)

    cart_page.verify_cart_is_empty()

    print(f"\nProduct removed successfully: {product_name}")


@pytest.mark.parametrize(
    "product",
    load_product_configurations(),
    ids=make_product_test_id,
)
def test_continue_shopping(
    product,
    authenticated_page,
    products_page,
    cart_page,
):
    """Verify that Continue Shopping returns to Products."""

    product_name = product["product_name"]

    products_page.add_product_to_cart(product_name)
    products_page.open_cart()

    cart_page.verify_cart_page()
    cart_page.continue_shopping()

    products_page.verify_products_page()

    print("\nContinue Shopping returned to Products page.")


def test_cart_is_empty_after_removing_product(
    authenticated_page,
    products_page,
    cart_page,
):
    """Verify that the cart has zero items after removal."""

    product_name = "Fleece Jacket"

    products_page.add_product_to_cart(product_name)
    products_page.open_cart()

    cart_page.remove_product(product_name)
    cart_page.verify_cart_is_empty()

    assert cart_page.get_cart_item_count() == 0

    print("\nCart is empty after removing the product.")
