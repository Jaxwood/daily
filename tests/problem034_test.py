import unittest
from problems.problem034 import palindrome


class TestProblem034(unittest.TestCase):

    def test_palindrome(self):
        expected = "ecarace"
        actual = palindrome("race")
        self.assertEqual(actual, expected)
