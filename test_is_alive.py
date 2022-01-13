from unittest import TestCase
from game import is_alive, make_spaceship
from unittest.mock import patch


class TestIsAlive(TestCase):

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_is_alive_spaceship_just_created(self, _):
        ship = make_spaceship()
        actual_value = is_alive(ship)
        self.assertTrue(actual_value)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_is_alive_spaceship_negative_hp(self, _):
        ship = make_spaceship()
        ship["currentHP"] = -1
        actual_value = is_alive(ship)
        self.assertFalse(actual_value)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_is_alive_spaceship_zero_hp(self, _):
        ship = make_spaceship()
        ship["currentHP"] = 0
        actual_value = is_alive(ship)
        self.assertFalse(actual_value)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_is_alive_spaceship_positive_hp(self, _):
        ship = make_spaceship()
        ship["currentHP"] = 23
        actual_value = is_alive(ship)
        self.assertTrue(actual_value)
