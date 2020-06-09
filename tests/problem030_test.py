import unittest
from problems.problem030 import units_of_water


class TestProblem030(unittest.TestCase):

    def test_units_of_water_single(self):
        expected = 1
        actual = units_of_water([2, 1, 2])
        self.assertEqual(actual, expected)

    def test_units_of_water_multiple(self):
        expected = 8
        actual = units_of_water([3, 0, 1, 3, 0, 5])
        self.assertEqual(actual, expected)
