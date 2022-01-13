from unittest import TestCase
from game import make_asteroid_belt_zone_in_board


class TestMakeAsteroidBeltZoneInBoard(TestCase):
    def test_make_asteroid_belt_zone_in_board_correct_coordinates(self):
        test_board = {}
        rows = 25
        for x_coordinate in range(0, rows):
            for y_coordinate in range(0, rows):
                test_board[(x_coordinate, y_coordinate)] = "Test Description"

        coordinates = (10, 10)
        make_asteroid_belt_zone_in_board(test_board, rows, coordinates)
        self.assertEqual(test_board[coordinates], "Asteroid Belt")

    def test_make_asteroid_belt_zone_in_board_wrong_coordinates(self):
        board = {}
        rows = 25
        for x_coordinate in range(0, rows):
            for y_coordinate in range(0, rows):
                board[(x_coordinate, y_coordinate)] = "Test Description"

        coordinates = (24, 24)
        make_asteroid_belt_zone_in_board(board, rows, coordinates)
        self.assertNotEqual(board[coordinates], "Asteroid Belt")
