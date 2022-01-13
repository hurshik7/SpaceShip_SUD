from unittest import TestCase
from game import user_choice_in_battle
from unittest.mock import patch


class TestUserChoiceInBattle(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_user_choice_in_battle_valid_input_fight(self, _):
        user_choice = user_choice_in_battle("Test Ship", "Test foe")
        self.assertEqual(user_choice, True)

    @patch('builtins.input', side_effect=['2'])
    def test_user_choice_in_battle_valid_input_flee(self, _):
        user_choice = user_choice_in_battle("Test Ship", "Test foe")
        self.assertEqual(user_choice, False)

    @patch('builtins.input', side_effect=['44', '111', '34', 3, '1'])
    def test_user_choice_in_battle_invalid_input(self, _):
        user_choice = user_choice_in_battle("Test Ship", "Test foe")
        self.assertEqual(user_choice, True)
