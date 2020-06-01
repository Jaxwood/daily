import unittest
from problems.problem021 import schedule


class TestProblem021(unittest.TestCase):

    def test_schedule(self):
        self.assertEqual(schedule([(30, 75), (0, 50), (60, 150)]), 2)