import unittest
from problems.problem006 import XORLinkedList


class TestProblem006(unittest.TestCase):

    def test_xorlinkedlist_add(self):
        xor = XORLinkedList()
        xor.add(3)
        xor.add(4)
        xor.add(5)
        xor.add(6)
        self.assertEqual(xor.get(2), 5)