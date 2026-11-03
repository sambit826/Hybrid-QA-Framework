"""
Locators for the SauceDemo Cart page.
"""


class CartLocators:

    PAGE_HEADING = '[data-test="title"]'

    CART_ITEMS = '[data-test="inventory-item"]'
    ITEM_NAME = '[data-test="inventory-item-name"]'
    ITEM_PRICE = '[data-test="inventory-item-price"]'

    REMOVE_BUTTON = 'button[data-test^="remove-"]'

    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CHECKOUT_BUTTON = '[data-test="checkout"]'