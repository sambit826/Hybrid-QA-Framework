
"""
Centralized test data and constants for SauceDemo automation.
"""

# --------------------------------------------------
# Browser configuration
# --------------------------------------------------

DEFAULT_BROWSER = "chromium"

SUPPORTED_BROWSERS = ("chromium", "firefox", "webkit")


# --------------------------------------------------
# Login test data
# --------------------------------------------------

VALID_LOGIN = {
    "username": "standard_user",
    "password": "secret_sauce",
}

LOCKED_OUT_LOGIN = {
    "username": "locked_out_user",
    "password": "secret_sauce",
}

EXPECTED_LOGIN_ERROR = (
    "Epic sadface: Sorry, this user has been locked out."
)


# --------------------------------------------------
# Product test data
# --------------------------------------------------

PRODUCT_CONFIGURATIONS = [
    {
        "number": 1,
        "product_name": "Fleece Jacket",
        "expected_product_name": "Sauce Labs Fleece Jacket",
        "browser": "firefox",
    },
    {
        "number": 2,
        "product_name": "Bolt T-Shirt",
        "expected_product_name": "Sauce Labs Bolt T-Shirt",
        "browser": "webkit",
    },
    {
        "number": 3,
        "product_name": "Onesie",
        "expected_product_name": "Sauce Labs Onesie",
        "browser": "chromium",
    },
]


def load_product_configurations():
    """Return a copy of the configured product data."""
    return [product.copy() for product in PRODUCT_CONFIGURATIONS]


# --------------------------------------------------
# Product sorting options
# --------------------------------------------------

SORT_OPTIONS = {
    "NAME_A_TO_Z": "az",
    "NAME_Z_TO_A": "za",
    "PRICE_LOW_TO_HIGH": "lohi",
    "PRICE_HIGH_TO_LOW": "hilo",
}


# --------------------------------------------------
# Checkout test data
# --------------------------------------------------

CHECKOUT_CUSTOMER = {
    "first_name": "Test",
    "last_name": "User",
    "postal_code": "751001",
}


# --------------------------------------------------
# Expected application messages
# --------------------------------------------------

EXPECTED_TEXT = {
    "products_page_heading": "Products",
    "cart_page_heading": "Your Cart",
    "checkout_page_heading": "Checkout: Your Information",
    "order_confirmation_heading": "Thank you for your order!",
    "order_confirmation_message": (
        "Your order has been dispatched, and will arrive "
        "just as fast as the pony can get there!"
    ),
}


# --------------------------------------------------
# Application URL paths
# --------------------------------------------------

URL_PATHS = {
    "login": "/",
    "inventory": "/inventory.html",
    "cart": "/cart.html",
    "checkout_step_one": "/checkout-step-one.html",
    "checkout_step_two": "/checkout-step-two.html",
    "checkout_complete": "/checkout-complete.html",
}
