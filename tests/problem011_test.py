import unittest
from problems.problem011 import Node, autocomplete


class TestProblem011(unittest.TestCase):

    def test_autocomplete(self):
        m = {
            'd': Node(
                {'o': Node(
                    {'g': None}, True),
                 'e': Node(
                    {'a': Node(
                        {'l': None}, True),
                     'e': Node(
                        {'r': None}, True)}, False)}, False)}
        trie = Node(m, False)
        self.assertEqual(autocomplete(trie, "de"), ["deal", "deer"])
