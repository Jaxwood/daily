import unittest
from problems.problem022 import words


class TestProblem022(unittest.TestCase):

    def test_words(self):
        w = ['quick', 'brown', 'the', 'fox']
        self.assertEqual(words(w, "thequickbrownfox"), ['the', 'quick', 'brown', 'fox'])

    def test_words_multiple(self):
        w = ['bed', 'bath', 'bedbath', 'and', 'beyond']
        self.assertEqual(words(w, "bedbathandbeyond"), ['bed', 'bath', 'and', 'beyond'])

    def test_words_impossible(self):
        w = ['bed', 'and', 'beyond']
        self.assertEqual(words(w, "bedbathandbeyond"), None)