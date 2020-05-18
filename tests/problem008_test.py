import unittest
from problems.problem008 import Node, unival


class TestProblem008(unittest.TestCase):

    def test_unival(self):
        tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
        self.assertEqual(unival(tree), 5)
