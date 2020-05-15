import unittest
from problems.problem004 import missing


class TestProblem003(unittest.TestCase):

    def test_missing_withoutDuplicates_returnsCorrectValue(self):
        self.assertEqual(missing([3, 4, -1, 1]),  2)

    def test_missing_withDuplicates_returnsCorrectValue(self):
        self.assertEqual(missing([1, 2, 2, 0]),  3)

    def test_missing_fullRange_returnsCorrectValue(self):
        self.assertEqual(missing([1, 2, 3]),  4)
