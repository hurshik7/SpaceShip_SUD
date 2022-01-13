from unittest import TestCase
from game import display_classes
from unittest.mock import patch
import io


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_classes(self, mock_output):
        display_classes()
        actual_output = mock_output.getvalue()
        expected_output = "1. Queen Jet: uses razor beam, was made of Adamantium\n"
        expected_output += "2. Battle Cruiser: uses vulcan cannon, was made of Graphene\n"
        expected_output += "3. Endurance: equip with guided missiles, was made of reinforced Aluminum\n"
        expected_output += "4. USCSS Prometheus: uses shotgun and flamethrower, was made of Vibranium\n"
        self.assertEqual(actual_output, expected_output)

