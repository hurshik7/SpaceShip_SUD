from unittest import TestCase
from game import display_level_up_message
from unittest.mock import patch
import io


class TestDisplayLevelUpMessage(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_level_up_message(self, mock_output):
        display_level_up_message(2)
        actual_output = mock_output.getvalue()
        expected_output = "\n**********************************************************************\n"
        expected_output += "Congratulation! Level-up! Your level now : 2!\nYour spaceship's attack, defense, "
        expected_output += "and max hp point was increased!\n"
        expected_output += "**********************************************************************\n"
        self.assertEqual(actual_output, expected_output)
