import unittest
from problems.problem014 import monte_carlo


class TestProblem014(unittest.TestCase):

    def test_monte_carlo(self):
        self.assertEqual(monte_carlo(20000000), 3.141)