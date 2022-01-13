from unittest import TestCase
from game import get_user_choice
from unittest.mock import patch


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_number_input_1(self, _):
        actual_value = get_user_choice()
        expected_value = 'N'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['2'])
    def test_get_user_choice_number_input_2(self, _):
        actual_value = get_user_choice()
        expected_value = 'S'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['3'])
    def test_get_user_choice_number_input_3(self, _):
        actual_value = get_user_choice()
        expected_value = 'W'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['4'])
    def test_get_user_choice_number_input_4(self, _):
        actual_value = get_user_choice()
        expected_value = 'E'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['N'])
    def test_get_user_choice_valid_input_upper_case_character(self, _):
        actual_value = get_user_choice()
        expected_value = 'N'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['s'])
    def test_get_user_choice_valid_input_lower_case_character(self, _):
        actual_value = get_user_choice()
        expected_value = 'S'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['souTh'])
    def test_get_user_choice_valid_input_word(self, _):
        actual_value = get_user_choice()
        expected_value = 'S'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['q'])
    def test_get_user_choice_valid_input_quit(self, _):
        actual_value = get_user_choice()
        expected_value = 'Q'
        self.assertEqual(actual_value, expected_value)

    @patch('builtins.input', side_effect=['qasdfwef', "hello", "I want quit", 'q'])
    def test_get_user_choice_invalid_input(self, _):
        actual_value = get_user_choice()
        expected_value = 'Q'
        self.assertEqual(actual_value, expected_value)
