import unittest
from problems.problem025 import matches


class TestProblem025(unittest.TestCase):

    def test_regex(self):
        self.assertEqual(matches('ray', 'ra.'), True)
        self.assertEqual(matches('raymond', 'ra.'), False)
        self.assertEqual(matches('chat', '.*at'), True)
        self.assertEqual(matches('chats', 'ra.'), False)