import unittest
from problems.problem020 import intersect_node


class TestProblem020(unittest.TestCase):

    def test_intersect_node(self):
        self.assertEqual(intersect_node([3,7,8,10], [99,1,8,10]), 8)