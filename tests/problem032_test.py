import unittest
from problems.problem032 import arbitrage


class TestProblem032(unittest.TestCase):

    def test_arbitrage(self):
        expected = True
        actual = arbitrage([[0.1, 1.9], [1.3, 0.5]])
        self.assertEqual(actual, expected)
