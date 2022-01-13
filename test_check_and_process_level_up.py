from unittest import TestCase
from game import check_and_process_level_up, make_spaceship
from unittest.mock import patch


class TestCheckAndProcessLevelUp(TestCase):

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_check_and_process_level_up_enough_experience(self, _):
        ship = make_spaceship()
        ship['exp'] = 1050
        check_and_process_level_up(ship)
        self.assertEqual(ship['level'], 2)

    @patch('builtins.input', side_effect=['TestName2', '1'])
    def test_check_and_process_level_up_not_enough_experience(self, _):
        ship = make_spaceship()
        ship['exp'] = 999
        check_and_process_level_up(ship)
        self.assertEqual(ship['level'], 1)

    @patch('builtins.input', side_effect=['TestName3', '2'])
    def test_check_and_process_level_up_too_much_experience(self, _):
        ship = make_spaceship()
        ship['exp'] = 10000
        check_and_process_level_up(ship)
        self.assertEqual(ship['level'], 5)
