
"""
Login test cases for SauceDemo.
"""

from config import (
    BASE_URL,
    SAUCEDEMO_USERNAME,
    SAUCEDEMO_PASSWORD,
)

from setup_blocks.constants import (
    LOCKED_OUT_LOGIN,
    EXPECTED_LOGIN_ERROR,
)


def test_valid_login(login_page, products_page):
    """Verify that a valid user can log in successfully."""

    login_page.open(BASE_URL)

    login_page.login(
        SAUCEDEMO_USERNAME,
        SAUCEDEMO_PASSWORD,
    )

    products_page.verify_products_page()

    print("\nValid login successful.")


def test_locked_out_login(login_page):
    """Verify that a locked-out user cannot log in."""

    login_page.open(BASE_URL)

    login_page.login(
        LOCKED_OUT_LOGIN["username"],
        LOCKED_OUT_LOGIN["password"],
    )

    login_page.verify_login_error(
        EXPECTED_LOGIN_ERROR
    )

    print("\nLocked-out login error verified.")
