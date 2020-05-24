import unittest
from problems.problem013 import distinct_sequence


class TestProblem013(unittest.TestCase):

    def test_distinct_sequence(self):
        self.assertEqual(distinct_sequence(2, "abcba"), 3)