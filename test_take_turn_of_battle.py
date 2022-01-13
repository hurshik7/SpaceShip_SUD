from unittest import TestCase
from game import take_turn_of_battle, make_foes, make_spaceship
from unittest.mock import patch
import io


class TestTakeTurnOfBattle(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_take_turn_of_battle_both_alive(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        take_turn_of_battle(ship, foe)
        expected_hp_of_ship_and_foe = (98, 52)
        actual_hp_of_ship_and_foe = (ship["currentHP"], foe["HP"])
        self.assertEqual(actual_hp_of_ship_and_foe, expected_hp_of_ship_and_foe)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    @patch('random.sample', return_value="Ultron")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_take_turn_of_battle_foe_die(self, mock_output, _, __):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        foe["HP"] = 10
        take_turn_of_battle(ship, foe)
        expected_output = "Ultron is destroyed! You won!"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    @patch('random.sample', return_value="Ultron")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_take_turn_of_battle_foe_die(self, mock_output, _, __):
        ship = make_spaceship()
        ship["currentHP"] = 2
        foe = make_foes("Solar System")
        take_turn_of_battle(ship, foe)
        expected_output = "Test Name is in danger! Mayday! Try to flee!"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
