import unittest
from problems.problem003 import Node, serialize, deserialize


class TestProblem003(unittest.TestCase):

    def test_node_serializeDeserialize_returnCorrectValues(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(deserialize(
            serialize(node)).left.left.val,  'left.left')
        self.assertEqual(deserialize(serialize(node)).right.val,  'right')
