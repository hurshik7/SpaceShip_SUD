from unittest import TestCase
from game import is_multiple_of_3


class TestIsMultipleOf3(TestCase):
    def test_is_multiple_of_3_positive_integer(self):
        self.assertTrue(is_multiple_of_3(81))

    def test_is_multiple_of_3_zero(self):
        self.assertTrue(is_multiple_of_3(0))

    def test_is_multiple_of_3_negative_integer(self):
        self.assertTrue(is_multiple_of_3(-3))
