from unittest import TestCase
from game import level_up_skill, make_spaceship
from unittest.mock import patch


class TestLevelUpSkill(TestCase):

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_level_up_skill_2_queenzet(self, _):
        ship = make_spaceship()
        ship['level'] = 2
        level_up_skill(ship)
        expected_skill = "Enhanced Laser Shot"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_level_up_skill_3_queenzet(self, _):
        ship = make_spaceship()
        ship['level'] = 3
        level_up_skill(ship)
        expected_skill = "Double Enhanced Laser Shot"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_level_up_skill_4_queenzet(self, _):
        ship = make_spaceship()
        ship['level'] = 4
        level_up_skill(ship)
        expected_skill = "Triple Mastered Laser Beam"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_level_up_skill_2_battlecruiser(self, _):
        ship = make_spaceship()
        ship['level'] = 2
        level_up_skill(ship)
        expected_skill = "Yamato Cannon"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_level_up_skill_3_battlecruiser(self, _):
        ship = make_spaceship()
        ship['level'] = 3
        level_up_skill(ship)
        expected_skill = "Double Yamato Cannon"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '2'])
    def test_level_up_skill_4_battlecruiser(self, _):
        ship = make_spaceship()
        ship['level'] = 4
        level_up_skill(ship)
        expected_skill = "Mastered Yamato Cannon"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '3'])
    def test_level_up_skill_2_endurance(self, _):
        ship = make_spaceship()
        ship['level'] = 2
        level_up_skill(ship)
        expected_skill = "Double Guided Missiles"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '3'])
    def test_level_up_skill_3_endurance(self, _):
        ship = make_spaceship()
        ship['level'] = 3
        level_up_skill(ship)
        expected_skill = "Triple Guided Missiles"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '3'])
    def test_level_up_skill_4_endurance(self, _):
        ship = make_spaceship()
        ship['level'] = 4
        level_up_skill(ship)
        expected_skill = "Triple Hellfire Missiles"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '4'])
    def test_level_up_skill_2_uscss(self, _):
        ship = make_spaceship()
        ship['level'] = 2
        level_up_skill(ship)
        expected_skill = "Blue Fire Shot Gun"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '4'])
    def test_level_up_skill_3_uscss(self, _):
        ship = make_spaceship()
        ship['level'] = 3
        level_up_skill(ship)
        expected_skill = "U-232 Shot Gun"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '4'])
    def test_level_up_skill_4_uscss(self, _):
        ship = make_spaceship()
        ship['level'] = 4
        level_up_skill(ship)
        expected_skill = "Triple U-232 Blue Fire Shot Gun"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_level_up_skill_over_4_queenzet(self, _):
        ship = make_spaceship()
        ship['level'] = 5
        level_up_skill(ship)
        expected_skill = "Triple Mastered Laser Beam"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)

    @patch('builtins.input', side_effect=['TestName', '1'])
    def test_level_up_skill_invalid_level(self, _):
        ship = make_spaceship()
        ship['level'] = -1
        level_up_skill(ship)
        expected_skill = "Enhanced Laser Shot"
        actual_skill = ship['skill']
        self.assertEqual(expected_skill, actual_skill)
