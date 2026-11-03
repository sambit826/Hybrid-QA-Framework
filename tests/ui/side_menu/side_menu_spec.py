
def test_open_side_menu(
    authenticated_page,
    side_menu_page,
):
    side_menu_page.open_menu()

    side_menu_page.verify_menu_is_open()

    print("\nSide menu opened successfully.")


def test_open_dynamic_catalog(
    authenticated_page,
    side_menu_page,
):
    side_menu_page.open_menu()
    side_menu_page.verify_menu_is_open()

    side_menu_page.open_dynamic_catalog()
    side_menu_page.verify_dynamic_catalog_options()

    print("\nDynamic Catalog expanded successfully.")


def test_open_lazy_load(
    authenticated_page,
    side_menu_page,
):
    side_menu_page.open_menu()
    side_menu_page.open_dynamic_catalog()
    side_menu_page.open_lazy_load()

    print("\nLazy Load option clicked successfully.")
    print(f"Current page URL: {authenticated_page.url}")


def test_open_spinner(
    authenticated_page,
    side_menu_page,
):
    side_menu_page.open_menu()
    side_menu_page.open_dynamic_catalog()
    side_menu_page.open_spinner()

    print("\nSpinner option clicked successfully.")
    print(f"Current page URL: {authenticated_page.url}")


def test_logout(
    authenticated_page,
    side_menu_page,
):
    side_menu_page.open_menu()
    side_menu_page.logout()

    side_menu_page.verify_logout()

    print("\nLogout verified successfully.")