from unittest import TestCase
from game import move_spaceship, make_spaceship
from unittest.mock import patch


class TestMoveSpaceship(TestCase):

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_move_spaceship_south(self, _):
        ship = make_spaceship()
        move_spaceship('S', ship)
        actual_location = (ship["x-coordinate"], ship["y-coordinate"])
        expected_location = (1, 0)
        self.assertEqual(actual_location, expected_location)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_move_spaceship_east(self, _):
        ship = make_spaceship()
        move_spaceship('E', ship)
        actual_location = (ship["x-coordinate"], ship["y-coordinate"])
        expected_location = (0, 1)
        self.assertEqual(actual_location, expected_location)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_move_spaceship_north(self, _):
        ship = make_spaceship()
        move_spaceship('N', ship)
        actual_location = (ship["x-coordinate"], ship["y-coordinate"])
        expected_location = (-1, 0)
        self.assertEqual(actual_location, expected_location)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_move_spaceship_west(self, _):
        ship = make_spaceship()
        move_spaceship('W', ship)
        actual_location = (ship["x-coordinate"], ship["y-coordinate"])
        expected_location = (0, -1)
        self.assertEqual(actual_location, expected_location)
