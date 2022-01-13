from unittest import TestCase
from game import user_attack_foe, make_foes, make_spaceship
from unittest.mock import patch


class TestUserAttackFoe(TestCase):

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_queenzet(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        user_attack_foe(ship, foe)
        expected_foe_hp = 52
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '2'])
    def test_user_attack_foe_battle_cruiser(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        user_attack_foe(ship, foe)
        expected_foe_hp = 42
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '3'])
    def test_user_attack_foe_endurance(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        user_attack_foe(ship, foe)
        expected_foe_hp = 67
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '4'])
    def test_user_attack_foe_uscss(self, _):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        user_attack_foe(ship, foe)
        expected_foe_hp = 27
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_with_worm_hole_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Worm Hole")
        user_attack_foe(ship, foe)
        expected_foe_hp = 63
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_with_nowhere_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Nowhere")
        user_attack_foe(ship, foe)
        expected_foe_hp = 74
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_with_vormir_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Vormir")
        user_attack_foe(ship, foe)
        expected_foe_hp = 85
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_with_titan_foe(self, _):
        ship = make_spaceship()
        foe = make_foes("Titan")
        user_attack_foe(ship, foe)
        expected_foe_hp = 95
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)

    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_user_attack_foe_with_boss(self, _):
        ship = make_spaceship()
        foe = make_foes("Boss")
        user_attack_foe(ship, foe)
        expected_foe_hp = 357
        actual_foe_hp = foe["HP"]
        self.assertEqual(expected_foe_hp, actual_foe_hp)
