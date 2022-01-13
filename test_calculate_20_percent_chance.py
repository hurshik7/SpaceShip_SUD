from unittest import TestCase
from game import calculate_20_percent_chance
from unittest.mock import patch


class TestCalculate20PercentChance(TestCase):

    @patch('random.randint', return_value=1)
    def test_calculate_20_percent_chance_win(self, _):
        actual_value = calculate_20_percent_chance()
        self.assertTrue(actual_value)

    @patch('random.randint', return_value=2)
    def test_calculate_20_percent_chance_lost(self, _):
        actual_value = calculate_20_percent_chance()
        self.assertFalse(actual_value)
