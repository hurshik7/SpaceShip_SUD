import io
from unittest import TestCase
from game import battle_with_foe, make_foes, make_spaceship
from unittest.mock import patch


class TestBattleWithFoe(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '1', '1', '1', '1'])
    def test_battle_with_foe_user_win(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        battle_with_foe(ship, foe)
        actual_exp_of_ship = ship["exp"]
        expected_exp_of_ship = 400
        self.assertEqual(actual_exp_of_ship, expected_exp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1', '2'])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_with_foe_user_flee(self, mock_output, _, __):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        battle_with_foe(ship, foe)
        expected_output = "You succeeded in escaping safely!"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Test Name', '1', '2'])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_with_foe_user_flee_get_hurt(self, _, __, ___):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        battle_with_foe(ship, foe)
        expected_hp_of_ship = 98
        actual_output = ship["currentHP"]
        self.assertEqual(expected_hp_of_ship, actual_output)

    @patch('builtins.input', side_effect=['Test Name', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_with_foe_win(self, mock_output, _):
        ship = make_spaceship()
        ship["currentHP"] = 1
        foe = make_foes("Solar System")
        battle_with_foe(ship, foe)
        expected_output = "Test Name is in danger! Mayday! Try to flee!"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)

    @patch('builtins.input', side_effect=['Test Name', '1', '2', '2', '1', '1', '1', '1', '1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_battle_with_foe_try_to_flee_boss(self, mock_output, _):
        ship = make_spaceship()
        foe = make_foes("Boss")
        battle_with_foe(ship, foe)
        expected_output = " You can NOT run away from the Sanctuary II"
        actual_output = mock_output.getvalue()
        self.assertIn(expected_output, actual_output)
