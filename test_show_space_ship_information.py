from unittest import TestCase
from game import show_space_ship_information
from unittest.mock import patch
import io


class TestShowSpaceShipInformation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_show_space_ship_information(self, mock_output):
        ship = {"name": "TestShip", "level": 1, "x-coordinate": 0, "y-coordinate": 0, "class": "QueenZet",
                "maxHP": 100, "attack": 50, "defence": 1, "skill": "Hyper Centered Laser Beam", "currentHP": 100,
                "exp": 1100}
        show_space_ship_information(ship)
        expected_output = """
Your Space ship \033[94mTestShip \033[0minfo :
----------------------------------------------------------------------
|             Name :                                 TestShip        |
|            Level :                                        1        |
|         Location :                                   (0, 0)        |
|            Class :                                 QueenZet        |
|           Max HP :                                      100        |
|       Current HP :                                      100        |
|           Attack :                                       50        |
|          Defence :                                        1        |
|            Skill :                Hyper Centered Laser Beam        |
|              Exp :                              1100 / 1000        |
----------------------------------------------------------------------\n"""
        self.assertEqual(expected_output, mock_output.getvalue())

