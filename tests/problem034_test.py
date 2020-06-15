import unittest
from problems.problem034 import palindrome, is_palindrome


class TestProblem034(unittest.TestCase):

    def test_is_palindrome(self):
        expected = "ecarace"
        self.assertEqual(True, is_palindrome(expected))

    def test_palindrome_race(self):
        expected = "ecarace"
        actual = palindrome("race")
        self.assertEqual(actual, expected)

    def test_palindrome_google(self):
        expected = "legoogel"
        actual = palindrome("legoog")
        self.assertEqual(actual, expected)
