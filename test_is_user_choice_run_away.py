from unittest import TestCase
from game import is_user_choice_run_away
from unittest.mock import patch


class TestIsUserChoiceRunAway(TestCase):

    @patch('builtins.input', side_effect=['y'])
    def test_is_user_choice_run_away_valid_input_choose_fight(self, _):
        foe = {'name': 'Test foe', 'attack': 1, 'defence': 1, 'exp': 1}
        user_choice = is_user_choice_run_away(foe)
        self.assertEqual(user_choice, False)

    @patch('builtins.input', side_effect=['N'])
    def test_is_user_choice_run_away_valid_input_choose_runaway(self, _):
        foe = {'name': 'Test foe', 'attack': 1, 'defence': 1, 'exp': 1}
        user_choice = is_user_choice_run_away(foe)
        self.assertEqual(user_choice, True)

    @patch('builtins.input', side_effect=['YN', "SEY", "123", '1', 1, 2, 3, "n"])
    def test_is_user_choice_run_away_invalid_input(self, _):
        foe = {'name': 'Test foe', 'attack': 1, 'defence': 1, 'exp': 1}
        user_choice = is_user_choice_run_away(foe)
        self.assertEqual(user_choice, True)
