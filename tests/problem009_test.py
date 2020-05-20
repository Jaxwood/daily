import unittest
from problems.problem009 import largest_sum


class TestProblem009(unittest.TestCase):

    def test_largest_sum(self):
        self.assertEqual(largest_sum([2, 4, 6, 2, 5]),  13)
