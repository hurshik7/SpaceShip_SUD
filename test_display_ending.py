from unittest import TestCase
from game import display_ending
from unittest.mock import patch
import io


class TestDisplayEnding(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_ending(self, mock_output):
        display_ending()
        actual_output = mock_output.getvalue()
        expected_output = "\n\033[95mYou defeated Sanctuary II and the universe is at peace."
        expected_output += "\nLost lives have returned. Well done. Everyone thank you for your hard work!"
        expected_output += "\n\n\nmade by Shik Hur, COMP1510 Assignment3\n"
        self.assertEqual(expected_output, actual_output)
