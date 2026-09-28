"""Tests for app.py. Run with: python -m unittest -v"""

import unittest

from app import price


class PriceTests(unittest.TestCase):
    def test_plan_without_promo(self):
        self.assertEqual(price("1gig"), 70.00)

    def test_promo_takes_20_dollars_off(self):
        self.assertEqual(price("1gig", "FIBER20"), 50.00)

    def test_unknown_promo_is_ignored(self):
        self.assertEqual(price("2gig", "FAKECODE"), 100.00)


if __name__ == "__main__":
    unittest.main()
