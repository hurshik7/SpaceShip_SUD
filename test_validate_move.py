from unittest import TestCase
from game import validate_move, make_spaceship, make_board
from unittest.mock import patch


class TestValidateMove(TestCase):

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_validate_move_out_of_boundary(self, _):
        board = make_board(25, 25)
        ship = make_spaceship()
        actual_value = validate_move(board, ship, 'N')
        self.assertFalse(actual_value)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_validate_move_valid_move(self, _):
        board = make_board(25, 25)
        ship = make_spaceship()
        actual_value = validate_move(board, ship, 'E')
        self.assertTrue(actual_value)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_validate_move_almost_destination(self, _):
        board = make_board(25, 25)
        ship = make_spaceship()
        ship["x-coordinate"] = 23
        ship["y-coordinate"] = 23
        actual_value = validate_move(board, ship, 'E')
        self.assertTrue(actual_value)
