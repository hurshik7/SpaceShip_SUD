from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board_25_by_25(self):
        actual_board = make_board(25, 25)
        expected_board = {(0, 0): 'Asteroid Belt', (0, 1): 'Solar System', (0, 2): 'Solar System',
                          (0, 3): 'Solar System', (0, 4): 'Solar System', (0, 5): 'Solar System', (0, 6): 'Worm Hole',
                          (0, 7): 'Worm Hole', (0, 8): 'Vormir', (0, 9): 'Vormir', (0, 10): 'Vormir',
                          (0, 11): 'Vormir', (0, 12): 'Vormir', (0, 13): 'Vormir', (0, 14): 'Vormir',
                          (0, 15): 'Vormir', (0, 16): 'Nowhere', (0, 17): 'Nowhere', (0, 18): 'Nowhere',
                          (0, 19): 'Nowhere', (0, 20): 'Titan', (0, 21): 'Titan', (0, 22): 'Titan', (0, 23): 'Titan',
                          (0, 24): 'Titan', (1, 0): 'Solar System', (1, 1): 'Solar System', (1, 2): 'Solar System',
                          (1, 3): 'Asteroid Belt', (1, 4): 'Solar System', (1, 5): 'Solar System',
                          (1, 6): 'Worm Hole', (1, 7): 'Worm Hole', (1, 8): 'Vormir', (1, 9): 'Vormir',
                          (1, 10): 'Vormir', (1, 11): 'Vormir', (1, 12): 'Vormir', (1, 13): 'Vormir',
                          (1, 14): 'Vormir', (1, 15): 'Vormir', (1, 16): 'Nowhere', (1, 17): 'Nowhere',
                          (1, 18): 'Nowhere', (1, 19): 'Nowhere', (1, 20): 'Titan', (1, 21): 'Titan',
                          (1, 22): 'Titan', (1, 23): 'Titan', (1, 24): 'Titan', (2, 0): 'Solar System',
                          (2, 1): 'Solar System', (2, 2): 'Solar System', (2, 3): 'Solar System',
                          (2, 4): 'Solar System', (2, 5): 'Solar System', (2, 6): 'Asteroid Belt',
                          (2, 7): 'Worm Hole', (2, 8): 'Vormir', (2, 9): 'Vormir', (2, 10): 'Vormir',
                          (2, 11): 'Vormir', (2, 12): 'Vormir', (2, 13): 'Vormir', (2, 14): 'Vormir',
                          (2, 15): 'Vormir', (2, 16): 'Nowhere', (2, 17): 'Nowhere', (2, 18): 'Nowhere',
                          (2, 19): 'Nowhere', (2, 20): 'Titan', (2, 21): 'Titan', (2, 22): 'Titan',
                          (2, 23): 'Titan', (2, 24): 'Titan', (3, 0): 'Solar System', (3, 1): 'Solar System',
                          (3, 2): 'Solar System', (3, 3): 'Solar System', (3, 4): 'Solar System',
                          (3, 5): 'Solar System', (3, 6): 'Worm Hole', (3, 7): 'Worm Hole', (3, 8): 'Vormir',
                          (3, 9): 'Asteroid Belt', (3, 10): 'Vormir', (3, 11): 'Vormir', (3, 12): 'Vormir',
                          (3, 13): 'Vormir', (3, 14): 'Vormir', (3, 15): 'Vormir', (3, 16): 'Nowhere',
                          (3, 17): 'Nowhere', (3, 18): 'Nowhere', (3, 19): 'Nowhere', (3, 20): 'Titan',
                          (3, 21): 'Titan', (3, 22): 'Titan', (3, 23): 'Titan', (3, 24): 'Titan',
                          (4, 0): 'Solar System', (4, 1): 'Solar System', (4, 2): 'Solar System',
                          (4, 3): 'Solar System', (4, 4): 'Solar System', (4, 5): 'Solar System',
                          (4, 6): 'Worm Hole', (4, 7): 'Worm Hole', (4, 8): 'Vormir', (4, 9): 'Vormir',
                          (4, 10): 'Vormir', (4, 11): 'Vormir', (4, 12): 'Asteroid Belt', (4, 13): 'Vormir',
                          (4, 14): 'Vormir', (4, 15): 'Vormir', (4, 16): 'Nowhere', (4, 17): 'Nowhere',
                          (4, 18): 'Nowhere', (4, 19): 'Nowhere', (4, 20): 'Titan', (4, 21): 'Titan',
                          (4, 22): 'Titan', (4, 23): 'Titan', (4, 24): 'Titan', (5, 0): 'Solar System',
                          (5, 1): 'Solar System', (5, 2): 'Solar System', (5, 3): 'Solar System',
                          (5, 4): 'Solar System', (5, 5): 'Solar System', (5, 6): 'Worm Hole', (
                              5, 7): 'Worm Hole', (5, 8): 'Vormir', (5, 9): 'Vormir', (5, 10): 'Vormir',
                          (5, 11): 'Vormir', (5, 12): 'Vormir', (5, 13): 'Vormir', (5, 14): 'Vormir',
                          (5, 15): 'Asteroid Belt', (5, 16): 'Nowhere', (5, 17): 'Nowhere', (5, 18): 'Nowhere',
                          (5, 19): 'Nowhere', (5, 20): 'Titan', (5, 21): 'Titan', (5, 22): 'Titan',
                          (5, 23): 'Titan', (5, 24): 'Titan', (6, 0): 'Worm Hole', (6, 1): 'Worm Hole',
                          (6, 2): 'Worm Hole', (6, 3): 'Worm Hole', (6, 4): 'Worm Hole', (6, 5): 'Worm Hole',
                          (6, 6): 'Worm Hole', (6, 7): 'Worm Hole', (6, 8): 'Vormir', (6, 9): 'Vormir',
                          (6, 10): 'Vormir', (6, 11): 'Vormir', (6, 12): 'Vormir', (6, 13): 'Vormir',
                          (6, 14): 'Vormir', (6, 15): 'Vormir', (6, 16): 'Nowhere', (6, 17): 'Nowhere',
                          (6, 18): 'Asteroid Belt', (6, 19): 'Nowhere', (6, 20): 'Titan', (6, 21): 'Titan',
                          (6, 22): 'Titan', (6, 23): 'Titan', (6, 24): 'Titan', (7, 0): 'Worm Hole',
                          (7, 1): 'Worm Hole', (7, 2): 'Worm Hole', (7, 3): 'Worm Hole', (7, 4): 'Worm Hole',
                          (7, 5): 'Worm Hole', (7, 6): 'Worm Hole', (7, 7): 'Worm Hole', (7, 8): 'Vormir',
                          (7, 9): 'Vormir', (7, 10): 'Vormir', (7, 11): 'Vormir', (7, 12): 'Vormir', (7, 13): 'Vormir',
                          (7, 14): 'Vormir', (7, 15): 'Vormir', (7, 16): 'Nowhere', (7, 17): 'Nowhere',
                          (7, 18): 'Nowhere', (7, 19): 'Nowhere', (7, 20): 'Titan', (7, 21): 'Asteroid Belt',
                          (7, 22): 'Titan', (7, 23): 'Titan', (7, 24): 'Titan', (8, 0): 'Vormir', (8, 1): 'Vormir',
                          (8, 2): 'Vormir', (8, 3): 'Vormir', (8, 4): 'Vormir', (8, 5): 'Vormir', (8, 6): 'Vormir',
                          (8, 7): 'Vormir', (8, 8): 'Vormir', (8, 9): 'Vormir', (8, 10): 'Vormir', (8, 11): 'Vormir',
                          (8, 12): 'Vormir', (8, 13): 'Vormir', (8, 14): 'Vormir', (8, 15): 'Vormir',
                          (8, 16): 'Nowhere', (8, 17): 'Nowhere', (8, 18): 'Nowhere', (8, 19): 'Nowhere',
                          (8, 20): 'Titan', (8, 21): 'Titan', (8, 22): 'Titan', (8, 23): 'Titan',
                          (8, 24): 'Asteroid Belt', (9, 0): 'Vormir', (9, 1): 'Vormir', (9, 2): 'Vormir',
                          (9, 3): 'Vormir', (9, 4): 'Vormir', (9, 5): 'Vormir', (9, 6): 'Vormir', (9, 7): 'Vormir',
                          (9, 8): 'Vormir', (9, 9): 'Vormir', (9, 10): 'Vormir', (9, 11): 'Vormir', (9, 12): 'Vormir',
                          (9, 13): 'Vormir', (9, 14): 'Vormir', (9, 15): 'Vormir', (9, 16): 'Nowhere',
                          (9, 17): 'Nowhere', (9, 18): 'Nowhere', (9, 19): 'Nowhere', (9, 20): 'Titan',
                          (9, 21): 'Titan', (9, 22): 'Titan', (9, 23): 'Titan', (9, 24): 'Titan', (10, 0): 'Vormir',
                          (10, 1): 'Vormir', (10, 2): 'Vormir', (10, 3): 'Vormir', (10, 4): 'Vormir', (10, 5): 'Vormir',
                          (10, 6): 'Vormir', (10, 7): 'Vormir', (10, 8): 'Vormir', (10, 9): 'Vormir',
                          (10, 10): 'Asteroid Belt', (10, 11): 'Vormir', (10, 12): 'Vormir', (10, 13): 'Vormir',
                          (10, 14): 'Vormir', (10, 15): 'Vormir', (10, 16): 'Nowhere', (10, 17): 'Nowhere',
                          (10, 18): 'Nowhere', (10, 19): 'Nowhere', (10, 20): 'Titan', (10, 21): 'Titan',
                          (10, 22): 'Titan', (10, 23): 'Titan', (10, 24): 'Titan', (11, 0): 'Vormir', (11, 1): 'Vormir',
                          (11, 2): 'Vormir', (11, 3): 'Vormir', (11, 4): 'Vormir', (11, 5): 'Vormir', (11, 6): 'Vormir',
                          (11, 7): 'Asteroid Belt', (11, 8): 'Vormir', (11, 9): 'Vormir', (11, 10): 'Vormir',
                          (11, 11): 'Vormir', (11, 12): 'Vormir', (11, 13): 'Asteroid Belt', (11, 14): 'Vormir',
                          (11, 15): 'Vormir', (11, 16): 'Nowhere', (11, 17): 'Nowhere', (11, 18): 'Nowhere',
                          (11, 19): 'Nowhere', (11, 20): 'Titan', (11, 21): 'Titan', (11, 22): 'Titan',
                          (11, 23): 'Titan', (11, 24): 'Titan', (12, 0): 'Vormir', (12, 1): 'Vormir', (12, 2): 'Vormir',
                          (12, 3): 'Vormir', (12, 4): 'Vormir', (12, 5): 'Vormir', (12, 6): 'Asteroid Belt',
                          (12, 7): 'Vormir', (12, 8): 'Vormir', (12, 9): 'Vormir', (12, 10): 'Vormir',
                          (12, 11): 'Vormir', (12, 12): 'Vormir', (12, 13): 'Vormir', (12, 14): 'Asteroid Belt',
                          (12, 15): 'Vormir', (12, 16): 'Nowhere', (12, 17): 'Nowhere', (12, 18): 'Nowhere',
                          (12, 19): 'Nowhere', (12, 20): 'Titan', (12, 21): 'Titan', (12, 22): 'Titan',
                          (12, 23): 'Titan', (12, 24): 'Titan', (13, 0): 'Vormir', (13, 1): 'Vormir', (13, 2): 'Vormir',
                          (13, 3): 'Vormir', (13, 4): 'Vormir', (13, 5): 'Vormir', (13, 6): 'Vormir', (13, 7): 'Vormir',
                          (13, 8): 'Vormir', (13, 9): 'Vormir', (13, 10): 'Vormir', (13, 11): 'Vormir',
                          (13, 12): 'Vormir', (13, 13): 'Vormir', (13, 14): 'Vormir', (13, 15): 'Vormir',
                          (13, 16): 'Nowhere', (13, 17): 'Nowhere', (13, 18): 'Nowhere', (13, 19): 'Nowhere',
                          (13, 20): 'Titan', (13, 21): 'Titan', (13, 22): 'Titan', (13, 23): 'Titan', (13, 24): 'Titan',
                          (14, 0): 'Vormir', (14, 1): 'Vormir', (14, 2): 'Vormir', (14, 3): 'Vormir', (14, 4): 'Vormir',
                          (14, 5): 'Vormir', (14, 6): 'Vormir', (14, 7): 'Vormir', (14, 8): 'Vormir', (14, 9): 'Vormir',
                          (14, 10): 'Vormir', (14, 11): 'Vormir', (14, 12): 'Vormir', (14, 13): 'Vormir',
                          (14, 14): 'Vormir', (14, 15): 'Vormir', (14, 16): 'Nowhere', (14, 17): 'Nowhere',
                          (14, 18): 'Nowhere', (14, 19): 'Nowhere', (14, 20): 'Titan', (14, 21): 'Titan',
                          (14, 22): 'Titan', (14, 23): 'Titan', (14, 24): 'Titan', (15, 0): 'Vormir', (15, 1): 'Vormir',
                          (15, 2): 'Vormir', (15, 3): 'Vormir', (15, 4): 'Vormir', (15, 5): 'Asteroid Belt',
                          (15, 6): 'Vormir', (15, 7): 'Vormir', (15, 8): 'Vormir', (15, 9): 'Vormir',
                          (15, 10): 'Vormir', (15, 11): 'Vormir', (15, 12): 'Vormir', (15, 13): 'Vormir',
                          (15, 14): 'Vormir', (15, 15): 'Asteroid Belt', (15, 16): 'Nowhere', (15, 17): 'Nowhere',
                          (15, 18): 'Nowhere', (15, 19): 'Nowhere', (15, 20): 'Titan', (15, 21): 'Titan',
                          (15, 22): 'Titan', (15, 23): 'Titan', (15, 24): 'Titan', (16, 0): 'Nowhere',
                          (16, 1): 'Nowhere', (16, 2): 'Nowhere', (16, 3): 'Nowhere', (16, 4): 'Nowhere',
                          (16, 5): 'Nowhere', (16, 6): 'Nowhere', (16, 7): 'Nowhere', (16, 8): 'Nowhere',
                          (16, 9): 'Nowhere', (16, 10): 'Nowhere', (16, 11): 'Nowhere', (16, 12): 'Nowhere',
                          (16, 13): 'Nowhere', (16, 14): 'Nowhere', (16, 15): 'Nowhere', (16, 16): 'Nowhere',
                          (16, 17): 'Nowhere', (16, 18): 'Nowhere', (16, 19): 'Nowhere', (16, 20): 'Titan',
                          (16, 21): 'Titan', (16, 22): 'Titan', (16, 23): 'Titan', (16, 24): 'Titan',
                          (17, 0): 'Nowhere', (17, 1): 'Nowhere', (17, 2): 'Nowhere', (17, 3): 'Nowhere',
                          (17, 4): 'Nowhere', (17, 5): 'Nowhere', (17, 6): 'Nowhere', (17, 7): 'Nowhere',
                          (17, 8): 'Nowhere', (17, 9): 'Nowhere', (17, 10): 'Nowhere', (17, 11): 'Nowhere',
                          (17, 12): 'Nowhere', (17, 13): 'Nowhere', (17, 14): 'Nowhere', (17, 15): 'Nowhere',
                          (17, 16): 'Nowhere', (17, 17): 'Nowhere', (17, 18): 'Nowhere', (17, 19): 'Nowhere',
                          (17, 20): 'Titan', (17, 21): 'Titan', (17, 22): 'Titan', (17, 23): 'Titan', (17, 24): 'Titan',
                          (18, 0): 'Nowhere', (18, 1): 'Nowhere', (18, 2): 'Nowhere', (18, 3): 'Nowhere',
                          (18, 4): 'Nowhere', (18, 5): 'Nowhere', (18, 6): 'Asteroid Belt', (18, 7): 'Nowhere',
                          (18, 8): 'Nowhere', (18, 9): 'Nowhere', (18, 10): 'Nowhere', (18, 11): 'Nowhere',
                          (18, 12): 'Nowhere', (18, 13): 'Nowhere', (18, 14): 'Asteroid Belt', (18, 15): 'Nowhere',
                          (18, 16): 'Nowhere', (18, 17): 'Nowhere', (18, 18): 'Nowhere', (18, 19): 'Nowhere',
                          (18, 20): 'Titan', (18, 21): 'Titan', (18, 22): 'Titan', (18, 23): 'Titan', (18, 24): 'Titan',
                          (19, 0): 'Nowhere', (19, 1): 'Nowhere', (19, 2): 'Nowhere', (19, 3): 'Nowhere',
                          (19, 4): 'Nowhere', (19, 5): 'Nowhere', (19, 6): 'Nowhere', (19, 7): 'Asteroid Belt',
                          (19, 8): 'Nowhere', (19, 9): 'Nowhere', (19, 10): 'Nowhere', (19, 11): 'Nowhere',
                          (19, 12): 'Nowhere', (19, 13): 'Asteroid Belt', (19, 14): 'Nowhere', (19, 15): 'Nowhere',
                          (19, 16): 'Nowhere', (19, 17): 'Nowhere', (19, 18): 'Nowhere', (19, 19): 'Nowhere',
                          (19, 20): 'Titan', (19, 21): 'Titan', (19, 22): 'Titan', (19, 23): 'Titan', (19, 24): 'Titan',
                          (20, 0): 'Titan', (20, 1): 'Titan', (20, 2): 'Titan', (20, 3): 'Titan', (20, 4): 'Titan',
                          (20, 5): 'Titan', (20, 6): 'Titan', (20, 7): 'Titan', (20, 8): 'Titan', (20, 9): 'Titan',
                          (20, 10): 'Asteroid Belt', (20, 11): 'Titan', (20, 12): 'Titan', (20, 13): 'Titan',
                          (20, 14): 'Titan', (20, 15): 'Titan', (20, 16): 'Titan', (20, 17): 'Titan', (20, 18): 'Titan',
                          (20, 19): 'Titan', (20, 20): 'Titan', (20, 21): 'Titan', (20, 22): 'Titan', (20, 23): 'Titan',
                          (20, 24): 'Titan', (21, 0): 'Titan', (21, 1): 'Titan', (21, 2): 'Titan', (21, 3): 'Titan',
                          (21, 4): 'Titan', (21, 5): 'Titan', (21, 6): 'Titan', (21, 7): 'Titan', (21, 8): 'Titan',
                          (21, 9): 'Titan', (21, 10): 'Titan', (21, 11): 'Titan', (21, 12): 'Titan', (21, 13): 'Titan',
                          (21, 14): 'Titan', (21, 15): 'Titan', (21, 16): 'Titan', (21, 17): 'Titan', (21, 18): 'Titan',
                          (21, 19): 'Titan', (21, 20): 'Titan', (21, 21): 'Titan', (21, 22): 'Titan', (21, 23): 'Titan',
                          (21, 24): 'Titan', (22, 0): 'Titan', (22, 1): 'Titan', (22, 2): 'Titan', (22, 3): 'Titan',
                          (22, 4): 'Titan', (22, 5): 'Titan', (22, 6): 'Titan', (22, 7): 'Titan', (22, 8): 'Titan',
                          (22, 9): 'Titan', (22, 10): 'Titan', (22, 11): 'Titan', (22, 12): 'Titan', (22, 13): 'Titan',
                          (22, 14): 'Titan', (22, 15): 'Titan', (22, 16): 'Titan', (22, 17): 'Titan', (22, 18): 'Titan',
                          (22, 19): 'Titan', (22, 20): 'Titan', (22, 21): 'Titan', (22, 22): 'Titan', (22, 23): 'Titan',
                          (22, 24): 'Titan', (23, 0): 'Titan', (23, 1): 'Titan', (23, 2): 'Titan', (23, 3): 'Titan',
                          (23, 4): 'Titan', (23, 5): 'Titan', (23, 6): 'Titan', (23, 7): 'Titan', (23, 8): 'Titan',
                          (23, 9): 'Titan', (23, 10): 'Titan', (23, 11): 'Titan', (23, 12): 'Titan', (23, 13): 'Titan',
                          (23, 14): 'Titan', (23, 15): 'Titan', (23, 16): 'Titan', (23, 17): 'Titan', (23, 18): 'Titan',
                          (23, 19): 'Titan', (23, 20): 'Titan', (23, 21): 'Titan', (23, 22): 'Titan', (23, 23): 'Titan',
                          (23, 24): 'Titan', (24, 0): 'Titan', (24, 1): 'Titan', (24, 2): 'Titan', (24, 3): 'Titan',
                          (24, 4): 'Titan', (24, 5): 'Titan', (24, 6): 'Titan', (24, 7): 'Titan', (24, 8): 'Titan',
                          (24, 9): 'Titan', (24, 10): 'Titan', (24, 11): 'Titan', (24, 12): 'Titan', (24, 13): 'Titan',
                          (24, 14): 'Titan', (24, 15): 'Titan', (24, 16): 'Titan', (24, 17): 'Titan', (24, 18): 'Titan',
                          (24, 19): 'Titan', (24, 20): 'Titan', (24, 21): 'Titan', (24, 22): 'Titan', (24, 23): 'Titan',
                          (24, 24): 'Boss'}
        self.assertEqual(actual_board, expected_board)

    def test_make_board_different_board_size(self):
        actual_board = make_board(5, 5)
        expected_board = {(0, 0): 'Asteroid Belt', (0, 1): 'Vormir', (0, 2): 'Vormir', (0, 3): 'Nowhere',
                          (0, 4): 'Titan', (1, 0): 'Vormir', (1, 1): 'Vormir', (1, 2): 'Vormir',
                          (1, 3): 'Asteroid Belt', (1, 4): 'Titan', (2, 0): 'Vormir', (2, 1): 'Vormir',
                          (2, 2): 'Vormir', (2, 3): 'Nowhere', (2, 4): 'Titan', (3, 0): 'Nowhere', (3, 1): 'Nowhere',
                          (3, 2): 'Nowhere', (3, 3): 'Nowhere', (3, 4): 'Titan', (4, 0): 'Titan', (4, 1): 'Titan',
                          (4, 2): 'Titan', (4, 3): 'Titan', (4, 4): 'Boss'}
        self.assertEqual(actual_board, expected_board)
