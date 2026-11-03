
"""
Generate and save authenticated SauceDemo browser storage state.
"""

import sys
from pathlib import Path

# Add the project root to Python's import search path.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from playwright.sync_api import sync_playwright

from config import (
    BASE_URL,
    SAUCEDEMO_USERNAME,
    SAUCEDEMO_PASSWORD,
)

from src.pages.saucedemo.login.login_page import LoginPage
from src.pages.saucedemo.products.products_page import ProductsPage


AUTH_DIRECTORY = PROJECT_ROOT / "auth"
AUTH_STATE_FILE = AUTH_DIRECTORY / "auth_state.json"


def save_authentication_state():
    """Log in to SauceDemo and save the authenticated browser state."""

    AUTH_DIRECTORY.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(
            headless=False,
            slow_mo=800,
        )

        try:
            context = browser.new_context()
            page = context.new_page()

            login_page = LoginPage(page)
            products_page = ProductsPage(page)

            print("\nSTEP 1: Opening SauceDemo login page.")

            login_page.open(BASE_URL)

            print("\nSTEP 2: Logging in to SauceDemo.")

            login_page.login(
                SAUCEDEMO_USERNAME,
                SAUCEDEMO_PASSWORD,
            )

            print("\nSTEP 3: Verifying successful login.")

            products_page.verify_products_page()

            print("Login successful.")

            print("\nSTEP 4: Saving authentication state.")

            context.storage_state(
                path=str(AUTH_STATE_FILE),
            )

            print(
                f"Authentication state saved successfully: "
                f"{AUTH_STATE_FILE}"
            )

            context.close()

        finally:
            browser.close()


if __name__ == "__main__":
    save_authentication_state()
