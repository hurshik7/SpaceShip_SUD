from unittest import TestCase
from game import ask_user_to_start_game
from unittest.mock import patch


class TestAskUserToStartGame(TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_ask_user_to_start_game_valid_input_character(self, _):
        actual_value = ask_user_to_start_game()
        self.assertTrue(actual_value)

    @patch('builtins.input', side_effect=['yeS'])
    def test_ask_user_to_start_game_valid_input_word(self, _):
        actual_value = ask_user_to_start_game()
        self.assertTrue(actual_value)

    @patch('builtins.input', side_effect=['yEssss'])
    def test_ask_user_to_start_game_invalid_input(self, _):
        actual_value = ask_user_to_start_game()
        self.assertFalse(actual_value)

    @patch('builtins.input', side_effect=['n'])
    def test_ask_user_to_start_game_valid_input_no(self, _):
        actual_value = ask_user_to_start_game()
        self.assertFalse(actual_value)
