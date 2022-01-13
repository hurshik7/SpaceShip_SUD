from unittest import TestCase
from game import check_if_goal_attained, make_foes


class TestIfGoalAttained(TestCase):
    def test_check_if_goal_attained_boss_just_created(self):
        boss = make_foes("Boss")
        actual_value = check_if_goal_attained(boss)
        self.assertFalse(actual_value)

    def test_check_if_goal_attained_boss_dead(self):
        boss = make_foes("Boss")
        boss["HP"] = 0
        actual_value = check_if_goal_attained(boss)
        self.assertTrue(actual_value)

    def test_check_if_goal_attained_boss_alive(self):
        boss = make_foes("Boss")
        boss["HP"] = 1
        actual_value = check_if_goal_attained(boss)
        self.assertFalse(actual_value)
