import unittest
from problems.problem031 import edit_distance


class TestProblem031(unittest.TestCase):

    def test_edit_distance(self):
        expected = 3
        actual = edit_distance("kitten", "sitting")
        self.assertEqual(actual, expected)
