from unittest import TestCase
from game import make_spaceship
from unittest.mock import patch


class TestMakeSpaceship(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_make_spaceship_valid_input(self, _):
        actual_ship = make_spaceship()
        expected_ship = {'attack': 50, 'class': 'QueenZet', 'currentHP': 100, 'defence': 3, 'exp': 0, 'level': 1,
                         'maxHP': 100, 'name': 'Test Name', 'skill': 'Hyper Centered Laser Beam', 'x-coordinate': 0,
                         'y-coordinate': 0}
        self.assertEqual(actual_ship, expected_ship)

    @patch('builtins.input', side_effect=['123lsdfj;lawenlvj0023jlskdflaslflsdlfjl', 'Test Name', '2'])
    def test_make_spaceship_invalid_input_too_long_character_name(self, _):
        ship = make_spaceship()
        expected_ship = {'attack': 60, 'class': 'BattleCruiser', 'currentHP': 95, 'defence': 2, 'exp': 0, 'level': 1,
                         'maxHP': 95, 'name': 'Test Name', 'skill': 'Bombard Vulcan Cannon', 'x-coordinate': 0,
                         'y-coordinate': 0}
        self.assertEqual(ship, expected_ship)

    @patch('builtins.input', side_effect=['Test Name', '5', '3'])
    def test_make_spaceship_invalid_input_wrong_class_selection(self, _):
        ship = make_spaceship()
        expected_ship = {'attack': 35, 'class': 'Endurance', 'currentHP': 140, 'defence': 1, 'exp': 0, 'level': 1,
                         'maxHP': 140, 'name': 'Test Name', 'skill': 'Guided Missiles', 'x-coordinate': 0,
                         'y-coordinate': 0}
        self.assertEqual(ship, expected_ship)
