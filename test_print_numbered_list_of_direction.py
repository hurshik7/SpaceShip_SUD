from unittest import TestCase
from game import print_numbered_list_of_direction
from unittest.mock import patch
import io


class TestPrintNumberedListOfDirection(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_numbered_list_of_direction(self, mock_output):
        print_numbered_list_of_direction()
        expected_output = "\nWhere are you heading ?\n1. North\n2. South\n3. West\n4. East"
        expected_output += "\nOr if you want to quit, enter 'Q'\n"
        self.assertEqual(mock_output.getvalue(), expected_output)
