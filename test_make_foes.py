from unittest import TestCase
from game import make_foes
from unittest.mock import patch


class TestMakeFoes(TestCase):

    @patch('random.sample', return_value='Ultron')
    def test_make_foes_in_solar_system_Ultron(self, _):
        actual_foe = make_foes("Solar System")
        expected_foe = {"name": "Ultron", "HP": 100, "attack": 5, "defence": 2, "exp": 400}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Ulysses')
    def test_make_foes_in_solar_system_Ulysses(self, _):
        actual_foe = make_foes("Solar System")
        expected_foe = {"name": "Ulysses", "HP": 100, "attack": 5, "defence": 2, "exp": 400}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Ivan Vanko')
    def test_make_foes_in_solar_system_Ivan(self, _):
        actual_foe = make_foes("Solar System")
        expected_foe = {"name": "Ivan Vanko", "HP": 100, "attack": 5, "defence": 2, "exp": 400}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Loki')
    def test_make_foes_in_worm_hole_loki(self, _):
        actual_foe = make_foes("Worm Hole")
        expected_foe = {"name": "Loki", "HP": 110, "attack": 10, "defence": 3, "exp": 700}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Chitauri')
    def test_make_foes_in_worm_hole_chitauri(self, _):
        actual_foe = make_foes("Worm Hole")
        expected_foe = {"name": "Chitauri", "HP": 110, "attack": 10, "defence": 3, "exp": 700}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Alien')
    def test_make_foes_in_worm_hole_alien(self, _):
        actual_foe = make_foes("Worm Hole")
        expected_foe = {"name": "Alien", "HP": 110, "attack": 10, "defence": 3, "exp": 700}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Ronan')
    def test_make_foes_in_nowhere_ronan(self, _):
        actual_foe = make_foes("Nowhere")
        expected_foe = {"name": "Ronan", "HP": 120, "attack": 15, "defence": 4, "exp": 1000}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Hela')
    def test_make_foes_in_nowhere_hela(self, _):
        actual_foe = make_foes("Nowhere")
        expected_foe = {"name": "Hela", "HP": 120, "attack": 15, "defence": 4, "exp": 1000}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Predator')
    def test_make_foes_in_nowhere_predator(self, _):
        actual_foe = make_foes("Nowhere")
        expected_foe = {"name": "Predator", "HP": 120, "attack": 15, "defence": 4, "exp": 1000}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Red Skull')
    def test_make_foes_in_vormir_red_skull(self, _):
        actual_foe = make_foes("Vormir")
        expected_foe = {"name": "Red Skull", "HP": 130, "attack": 18, "defence": 5, "exp": 1300}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Kang')
    def test_make_foes_in_vormir_kang(self, _):
        actual_foe = make_foes("Vormir")
        expected_foe = {"name": "Kang", "HP": 130, "attack": 18, "defence": 5, "exp": 1300}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Doctor Light')
    def test_make_foes_in_vormir_doctor_light(self, _):
        actual_foe = make_foes("Vormir")
        expected_foe = {"name": "Doctor Light", "HP": 130, "attack": 18, "defence": 5, "exp": 1300}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Ego')
    def test_make_foes_in_titan_ego(self, _):
        actual_foe = make_foes("Titan")
        expected_foe = {"name": "Ego", "HP": 140, "attack": 20, "defence": 5, "exp": 1500}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Doom')
    def test_make_foes_in_titan_doom(self, _):
        actual_foe = make_foes("Titan")
        expected_foe = {"name": "Doom", "HP": 140, "attack": 20, "defence": 5, "exp": 1500}
        self.assertEqual(expected_foe, actual_foe)

    @patch('random.sample', return_value='Jerico')
    def test_make_foes_in_titan_jerico(self, _):
        actual_foe = make_foes("Titan")
        expected_foe = {"name": "Jerico", "HP": 140, "attack": 20, "defence": 5, "exp": 1500}
        self.assertEqual(expected_foe, actual_foe)

    def test_make_foes_boss(self):
        actual_foe = make_foes("Boss")
        expected_foe = {"name": "Sanctuary II", "HP": 400, "attack": 25, "defence": 7, "exp": 3000}
        self.assertEqual(expected_foe, actual_foe)
