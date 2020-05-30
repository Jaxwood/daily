import unittest
from problems.problem018 import maximum_value


class TestProblem018(unittest.TestCase):

    def test_maximum_value(self):
        self.assertEqual(maximum_value([10, 5, 2, 7, 8, 7], 3), [10, 7, 8, 8])
