import pytest

from setup_blocks.constants import (
    load_product_configurations,
    CHECKOUT_CUSTOMER,
    EXPECTED_TEXT,
)


def make_checkout_test_id(product):
    return (
        f"checkout_product_{product['number']}_"
        f"{product['product_name'].lower().replace(' ', '_')}"
    )


@pytest.mark.parametrize(
    "product",
    load_product_configurations(),
    ids=make_checkout_test_id,
)
def test_complete_purchase(
    product,
    authenticated_page,
    products_page,
    cart_page,
    checkout_page,
):
    product_name = product["product_name"]

    print(f"\nStarting purchase test for: {product_name}")

    # Add the configured product to the cart.
    products_page.add_product_to_cart(product_name)

    # Open the cart and proceed to checkout.
    products_page.open_cart()
    cart_page.verify_cart_page()
    cart_page.proceed_to_checkout()

    # Enter customer information.
    checkout_page.enter_customer_information(
        CHECKOUT_CUSTOMER["first_name"],
        CHECKOUT_CUSTOMER["last_name"],
        CHECKOUT_CUSTOMER["postal_code"],
    )

    # Continue to the order overview.
    checkout_page.continue_to_overview()

    # Finish the order.
    checkout_page.finish_order()

    # Verify the order confirmation.
    checkout_page.verify_order_confirmation(
        EXPECTED_TEXT["order_confirmation_heading"],
        EXPECTED_TEXT["order_confirmation_message"],
    )

    # Print the confirmation details.
    confirmation_heading = checkout_page.get_confirmation_heading()
    confirmation_message = checkout_page.get_confirmation_message()

    print(f"\nOrder confirmation heading: {confirmation_heading}")
    print(f"Order confirmation message: {confirmation_message}")

    # Return to the Products page.
    checkout_page.back_to_products()
    products_page.verify_products_page()

    print(f"\nPurchase completed successfully for: {product_name}")