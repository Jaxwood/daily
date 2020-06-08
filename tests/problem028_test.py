import unittest
from problems.problem028 import justify


class TestProblem028(unittest.TestCase):

    def test_justify(self):
        self.assertEqual(justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16), ["the  quick brown", "fox  jumps  over", "the   lazy   dog"])