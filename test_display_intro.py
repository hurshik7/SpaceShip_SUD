from unittest import TestCase
from game import display_intro
from unittest.mock import patch
import io


class TestDisplayIntro(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_intro(self, mock_output):
        expected_output = f"""       
           !
           !
           ^
          / \\
         /___\\
        |=   =|
        |     |
        |     |  
        |     |
        |     |
       /|##!##|\\
      / |##!##| \\
     /  |##!##|  \\
    |  / ^ | ^ \\  |
    | /  ( | )  \\ |
    |/   ( | )   \\|  
        ((   ))
       ((  :  ))      Hello Avengers! 23 days ago Sanctuary II which is a giant space mother ship attacked Earth.
       ((  :  ))      Unfortunately, It took the core of Earth! The core is essential to all life in Earth!
        ((   ))       But few days ago, it is said that the Sanctuary II was detected in the Titan area.
         (( ))        Avengers!! It's time to assemble! The rest of the Avengers have already left to destroy it!
          ( )         Unfortunately again, they sent a rescue signal!
           .          Pack your suit and weapons! Check your battle spaceship! Embark on this journey! Hurry up!
           .
           .
    \n\n"""
        display_intro()
        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
