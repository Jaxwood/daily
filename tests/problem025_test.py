import unittest
from problems.problem025 import regex


class TestProblem025(unittest.TestCase):

    def test_regex(self):
        self.assertEqual(regex('ray', 'ra.'), True)
        self.assertEqual(regex('raymond', 'ra.'), False)
        self.assertEqual(regex('chat', '.*at'), True)
        self.assertEqual(regex('chats', 'ra.'), False)