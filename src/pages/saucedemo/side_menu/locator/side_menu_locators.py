"""
Locators for the SauceDemo Side Menu.
"""


class SideMenuLocators:

    # Main menu button
    MENU_BUTTON = '#react-burger-menu-btn'

    # Dynamic Catalog menu and submenu
    DYNAMIC_CATALOG_LINK = '[data-test="dynamic-catalog-sidebar-link"]'
    LAZY_LOAD_LINK = '[data-test="dynamic-catalog-lazy-load-link"]'
    SPINNER_LINK = '[data-test="dynamic-catalog-spinner-link"]'

    # Logout
    LOGOUT_LINK = '[data-test="logout-sidebar-link"]'