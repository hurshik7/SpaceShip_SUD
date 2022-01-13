from unittest import TestCase
from game import find_maximum_coordinate_of_board, make_board


class TestFindMaximumCoordinateOfBoard(TestCase):
    def test_find_maximum_coordinate_of_board_n_by_n_board(self):
        board = make_board(25, 25)
        actual_value = find_maximum_coordinate_of_board(board)
        expected_value = (24, 24)
        self.assertEqual(actual_value, expected_value)

    def test_find_maximum_coordinate_of_board_n_by_m_board(self):
        board = make_board(25, 20)
        actual_value = find_maximum_coordinate_of_board(board)
        expected_value = (24, 19)
        self.assertEqual(actual_value, expected_value)

    def test_find_maximum_coordinate_of_board_0_by_0_board(self):
        board = make_board(0, 0)
        actual_value = find_maximum_coordinate_of_board(board)
        expected_value = (0, 0)
        self.assertEqual(actual_value, expected_value)

    def test_find_maximum_coordinate_of_board_1_by_1_board(self):
        board = make_board(1, 1)
        actual_value = find_maximum_coordinate_of_board(board)
        expected_value = (0, 0)
        self.assertEqual(actual_value, expected_value)
