import unittest
from problems.problem024 import Node


class TestProblem024(unittest.TestCase):

    def test_binary_lock_tree(self):
        n = Node(1, False, Node(2), Node(3))
        self.assertEqual(n.is_locked(), False)
        self.assertEqual(n.lock(), True)
        self.assertEqual(n.unlock(), True)
        self.assertEqual(n.left.lock(), True)
        self.assertEqual(n.left.unlock(), True)
        self.assertEqual(n.left.lock(), True)
        self.assertEqual(n.lock(), False)