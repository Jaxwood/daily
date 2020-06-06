import unittest
from problems.problem026 import Node


class TestProblem026(unittest.TestCase):

    def test_regex(self):
        n = Node(1, Node(2, Node(3, Node(4))))
        nn = n.remove(0)
        self.assertEqual(nn.length(), 3)