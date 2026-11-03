
"""
Locators for SauceDemo Checkout pages.
"""


class CheckoutLocators:

    # Checkout information page
    FIRST_NAME_INPUT = '[data-test="firstName"]'
    LAST_NAME_INPUT = '[data-test="lastName"]'
    POSTAL_CODE_INPUT = '[data-test="postalCode"]'
    CONTINUE_BUTTON = '[data-test="continue"]'

    # Checkout overview page
    FINISH_BUTTON = '[data-test="finish"]'

    # Order confirmation page
    CONFIRMATION_HEADING = '[data-test="complete-header"]'
    CONFIRMATION_MESSAGE = '[data-test="complete-text"]'
    BACK_HOME_BUTTON = '[data-test="back-to-products"]'
