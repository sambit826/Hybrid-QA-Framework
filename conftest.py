
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright, Error as PlaywrightError

from config import (
    BASE_URL,
    SAUCEDEMO_USERNAME,
    SAUCEDEMO_PASSWORD,
)

from setup_blocks.constants import (
    DEFAULT_BROWSER,
    URL_PATHS,
)

from src.pages.saucedemo.login.login_page import LoginPage
from src.pages.saucedemo.products.products_page import ProductsPage
from src.pages.saucedemo.cart.cart_page import CartPage
from src.pages.saucedemo.checkout.checkout_page import CheckoutPage
from src.pages.saucedemo.side_menu.side_menu_page import SideMenuPage


PROJECT_ROOT = Path(__file__).resolve().parent
AUTH_STATE_FILE = PROJECT_ROOT / "auth" / "auth_state.json"


@pytest.fixture(scope="session")
def playwright_instance():
    """Start Playwright once for the test session."""
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def ui_browser(request, playwright_instance):
    """
    Launch the browser configured for the current product.
    If the test has a product parameter, use its browser.
    Otherwise, use DEFAULT_BROWSER.
    """
    browser_name = DEFAULT_BROWSER

    if "product" in request.fixturenames:
        product = request.getfixturevalue("product")
        browser_name = product["browser"]

    if browser_name not in ("chromium", "firefox", "webkit"):
        raise pytest.UsageError(
            f"Unsupported browser configured: {browser_name}"
        )

    browser_type = getattr(playwright_instance, browser_name)

    print(f"\nLaunching browser: {browser_name}")

    browser = browser_type.launch(
        headless=False,
        slow_mo=1000,
    )

    yield browser

    print(f"\nClosing browser: {browser_name}")
    browser.close()


@pytest.fixture
def ui_context(request, ui_browser):
    """
    Create an isolated browser context for each test.

    Authenticated tests reuse the saved authentication state.
    If the state is invalid or expired, log in again and save
    a refreshed authentication state.

    Login tests receive a fresh unauthenticated context.
    """

    requires_authentication = "authenticated_page" in request.fixturenames

    if not requires_authentication:
        context = ui_browser.new_context()

        yield context

        context.close()
        return

    print("\nChecking saved SauceDemo authentication state...")

    context = None

    # STEP 1: Try loading the existing authentication state.
    if AUTH_STATE_FILE.exists():

        try:
            context = ui_browser.new_context(
                storage_state=str(AUTH_STATE_FILE)
            )

            print("Saved authentication state loaded.")

        except (PlaywrightError, OSError, ValueError) as error:
            print(
                "\nSaved authentication state could not be loaded."
            )
            print(f"Reason: {error}")

    else:
        print("\nAuthentication state file not found.")

    # STEP 2: If no usable context was created, create a fresh one.
    if context is None:
        context = ui_browser.new_context()

    validation_page = context.new_page()

    try:
        # STEP 3: Check whether the saved session is still valid.
        inventory_url = (
            BASE_URL.rstrip("/")
            + URL_PATHS["inventory"]
        )

        validation_page.goto(inventory_url)

        products_page = ProductsPage(validation_page)

        if products_page.is_products_page():

            print(
                "\nSaved authentication session is valid."
            )

        else:
            # STEP 4: Session expired or is not authenticated.
            print(
                "\nAuthentication session is invalid or expired."
            )
            print("Starting a fresh SauceDemo login...")

            login_page = LoginPage(validation_page)

            login_page.open(BASE_URL)

            login_page.login(
                SAUCEDEMO_USERNAME,
                SAUCEDEMO_PASSWORD,
            )

            products_page.verify_products_page()

            print("\nRe-login successful.")

            # STEP 5: Save the refreshed authentication state.
            context.storage_state(
                path=str(AUTH_STATE_FILE)
            )

            print(
                "\nAuthentication state refreshed successfully."
            )

    except Exception:
        validation_page.close()
        context.close()
        raise

    validation_page.close()

    print("\nAuthenticated browser context is ready.")

    yield context

    context.close()


@pytest.fixture
def ui_page(ui_context):
    """Create a fresh browser page for each test."""
    page = ui_context.new_page()

    yield page

    page.close()


@pytest.fixture
def login_page(ui_page):
    return LoginPage(ui_page)


@pytest.fixture
def products_page(ui_page):
    return ProductsPage(ui_page)


@pytest.fixture
def cart_page(ui_page):
    return CartPage(ui_page)


@pytest.fixture
def checkout_page(ui_page):
    return CheckoutPage(ui_page)


@pytest.fixture
def side_menu_page(ui_page):
    return SideMenuPage(ui_page)


@pytest.fixture
def authenticated_page(
    login_page,
    products_page,
):
    """
    Open the inventory page using the authenticated context.
    Authentication is checked by the ui_context fixture.
    """

    inventory_url = (
        BASE_URL.rstrip("/")
        + URL_PATHS["inventory"]
    )

    login_page.page.goto(inventory_url)

    products_page.verify_products_page()

    print("\nAuthenticated Products page is ready.")

    return login_page.page
