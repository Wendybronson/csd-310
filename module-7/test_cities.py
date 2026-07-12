# ---------------------------------------------------------
# Wendy Bronson
# Module 7.2 Assignment: Test Cases
# Date: 07/08/2026
#
# Purpose:
# Unit tests for the city_country function.
# ---------------------------------------------------------

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does a city and country format correctly?"""
        result = city_country("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()