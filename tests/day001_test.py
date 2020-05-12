import unittest
from problems.day001 import hasSumOfPair

class TestDay001(unittest.TestCase):

    def test_hasSumOf_whenSumIsTrue_ForPairOfNumbers(self):
        self.assertTrue(hasSumOfPair([10, 15, 3, 7], 17))
    def test_hasSumOf_whenSumIsFalse(self):
        self.assertFalse(hasSumOfPair([10, 15, 3, 7], 19))