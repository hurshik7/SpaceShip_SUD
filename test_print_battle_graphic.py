from unittest import TestCase
from game import print_battle_graphic
from unittest.mock import patch
import io


class TestPrintBattleGraphic(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_battle_graphic(self, mock_output):
        print_battle_graphic()
        expected_output = """
                 .  . '    .
              '   .            . '            .                +
                      `                          '    . '
                .                         ,'`.                         .
           .                  .."    _.-;'    `.              .
                      _.-"`.##%"_.--" ,'        `.           "#"     ___,,od000
                   ,'"-_ _.-.--"\\   ,'            `-_       '%#%',,/////00000HH
                 ,'     |_.'     )`/-     __..--""`-_`-._    J L/////00000HHHHM
         . +   ,'   _.-"        / /   _-""           `-._`-_/___\\///0000HHHHMMM
             .'_.-""      '    :_/_.-'                 _,`-/__V__\0000HHHHHMMMM
         . _-""                         .        '   _,////\\  |  /000HHHHHMMMMM
        _-"   .       '  +  .              .        ,//////0\\ | /00HHHHHHHMMMMM
               `                                   ,//////000\\|/00HHHHHHHMMMMMM
        .             '       .  ' .   .       '  ,//////00000|00HHHHHHHHMMMMMM
             .             .    .    '           ,//////000000|00HHHHHHHMMMMMMM
                          .  '      .       .   ,///////000000|0HHHHHHHHMMMMMMM
          '             '        .    '         ///////000000000HHHHHHHHMMMMMMM
                            +  .  . '    .     ,///////000000000HHHHHHHMMMMMMMM
             '      .              '   .       ///////000000000HHHHHHHHMMMMMMMM
           '                  . '              ///////000000000HHHHHHHHMMMMMMMM
                                   .   '      ,///////000000000HHHHHHHHMMMMMMMM
               +         .        '   .    .  ////////000000000HHHHHHHHMMMMMMhs\n"""

        actual_output = mock_output.getvalue()
        self.assertEqual(expected_output, actual_output)
