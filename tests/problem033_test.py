import unittest
from problems.problem033 import median


class TestProblem033(unittest.TestCase):

    def test_median(self):
        expected = [2, 1.5, 2, 3.5, 2, 2, 2]
        actual = median([2, 1, 5, 7, 2, 0, 5])
        self.assertEqual(actual, expected)
