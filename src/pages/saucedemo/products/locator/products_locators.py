
"""
Locators for the SauceDemo Products page.
"""


class ProductsLocators:

    PAGE_HEADING = '[data-test="title"]'

    PRODUCT_CARDS = '[data-test="inventory-item"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'
    PRODUCT_PRICE = '[data-test="inventory-item-price"]'

    SORT_DROPDOWN = '[data-test="product-sort-container"]'

    CART_LINK = '[data-test="shopping-cart-link"]'
    CART_BADGE = '[data-test="shopping-cart-badge"]'
