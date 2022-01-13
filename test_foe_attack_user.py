from unittest import TestCase
from game import foe_attack_user, make_foes, make_spaceship
from unittest.mock import patch


class TestFoeAttackUser(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_solar_system_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 98
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_worm_hole_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Worm Hole")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 93
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_vormir_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Vormir")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 85
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_nowhere_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Nowhere")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 88
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_titan_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Titan")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 83
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_foe_attack_user_boss(self, _):
        ship = make_spaceship()
        foe = make_foes("Boss")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 78
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '2'])
    def test_foe_attack_user_solar_system_foe_battle_cruiser(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 92
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '3'])
    def test_foe_attack_user_worm_hole_foe_endurance(self, _):
        ship = make_spaceship()
        foe = make_foes("Worm Hole")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 131
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)

    @patch('builtins.input', side_effect=['Test Name', '4'])
    def test_foe_attack_user_vormir_foe_uscss(self, _):
        ship = make_spaceship()
        foe = make_foes("Vormir")
        foe_attack_user(foe, ship)
        actual_hp_of_ship = ship["currentHP"]
        expected_hp_of_ship = 67
        self.assertEqual(actual_hp_of_ship, expected_hp_of_ship)
