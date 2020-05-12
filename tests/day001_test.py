import unittest
from problems.day001 import hasSumOfPair

class TestDay001(unittest.TestCase):

    def test_hasSumOfPair_whenSumIsFound_returnTrue(self):
        self.assertTrue(hasSumOfPair([10, 15, 3, 7], 17))
    def test_hasSumOfPair_whenSumNotFound_returnFalse(self):
        self.assertFalse(hasSumOfPair([10, 15, 3, 7], 19))