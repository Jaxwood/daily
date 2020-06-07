import unittest
from problems.problem026 import Node, remove


class TestProblem026(unittest.TestCase):

    def test_remove(self):
        n = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        remove(n, 3)
        self.assertEqual(str(n), '[1, 2, 4, 5]')