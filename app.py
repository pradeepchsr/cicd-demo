"""A tiny app used to learn the CI/CD flow.

It calculates a monthly price after a promo code, and says which
environment and version it is running in.
"""

import os

PLANS = {"1gig": 70.00, "2gig": 100.00}
PROMOS = {"FIBER20": 20.00}


def price(plan, promo=None):
    """Monthly price for a plan, after an optional promo code."""
    total = PLANS[plan]
    if promo in PROMOS:
        total = total - PROMOS[promo]
    return round(total, 2)


def main():
    env = os.environ.get("APP_ENV", "local")
    version = os.environ.get("APP_VERSION", "dev-build")
    message = os.environ.get("APP_MESSAGE", "no environment message set")
    print(f"Running in: {env}")
    print(f"Version:    {version}")
    print(f"Message:    {message}")
    print(f"1gig with FIBER20 costs ${price('1gig', 'FIBER20'):.2f}/mo")


if __name__ == "__main__":
    main()
