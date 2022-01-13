from unittest import TestCase
from game import try_to_flee_from_foe, make_spaceship, make_foes
from unittest.mock import patch


class TestTryToFleeFromFoe(TestCase):

    @patch('random.randint', return_value=1)
    @patch('random.sample', return_value='Ultron')
    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_try_to_flee_from_foe_get_damage(self, _, __, ___):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        try_to_flee_from_foe(ship, foe)
        expected_hp_of_ship = 98
        actual_hp_of_ship = ship['currentHP']
        self.assertEqual(expected_hp_of_ship, actual_hp_of_ship)

    @patch('random.randint', return_value=2)
    @patch('random.sample', return_value='Ultron')
    @patch('builtins.input', side_effect=['Test Name', '1'])
    def test_try_to_flee_from_foe_successful_flee(self, _, __, ___):
        ship = make_spaceship()
        foe = make_foes("Solar System")
        try_to_flee_from_foe(ship, foe)
        expected_hp_of_ship = 100
        actual_hp_of_ship = ship['currentHP']
        self.assertEqual(expected_hp_of_ship, actual_hp_of_ship)
