from unittest import TestCase
from game import draw_map, make_spaceship, make_board
from unittest.mock import patch
import io


class TestDrawMap(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_spaceship_different_board_size(self, mock_output, _):
        board = make_board(5, 5)
        ship = make_spaceship()
        draw_map(board, ship)
        actual_output = mock_output.getvalue()
        expected_output = """
Select the class of your space ship
1. Queen Jet: uses razor beam, was made of Adamantium
2. Battle Cruiser: uses vulcan cannon, was made of Graphene
3. Endurance: equip with guided missiles, was made of reinforced Aluminum
4. USCSS Prometheus: uses shotgun and flamethrower, was made of Vibranium
-----
[94mX[0m[93m-[0m[93m-[0m[94m?[0m[95m"[0m
[93m-[0m[93m-[0m[93m-[0m⣿[95m"[0m
[93m-[0m[93m-[0m[93m-[0m[94m?[0m[95m"[0m
[94m?[0m[94m?[0m[94m?[0m[94m?[0m[95m"[0m
[95m"[0m[95m"[0m[95m"[0m[95m"[0m[31m"[0m
----- (⣿ : Asteroid Belt, You can NOT move to the area)\n"""
        self.assertEqual(actual_output, expected_output)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_draw_map_spaceship_locate_not_start_point(self, mock_output, _):
        board = make_board(5, 5)
        ship = make_spaceship()
        ship['x-coordinate'] = 3
        ship['y-coordinate'] = 4
        draw_map(board, ship)
        actual_output = mock_output.getvalue()
        expected_output = """
Select the class of your space ship
1. Queen Jet: uses razor beam, was made of Adamantium
2. Battle Cruiser: uses vulcan cannon, was made of Graphene
3. Endurance: equip with guided missiles, was made of reinforced Aluminum
4. USCSS Prometheus: uses shotgun and flamethrower, was made of Vibranium
-----
⣿[93m-[0m[93m-[0m[94m?[0m[95m"[0m
[93m-[0m[93m-[0m[93m-[0m⣿[95m"[0m
[93m-[0m[93m-[0m[93m-[0m[94m?[0m[95m"[0m
[94m?[0m[94m?[0m[94m?[0m[94m?[0m[94mX[0m
[95m"[0m[95m"[0m[95m"[0m[95m"[0m[31m"[0m
----- (⣿ : Asteroid Belt, You can NOT move to the area)\n"""
        self.assertEqual(actual_output, expected_output)
