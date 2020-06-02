import unittest
from problems.problem023 import shortest_path


class TestProblem023(unittest.TestCase):

    def test_shortest_path(self):
        m = [[False, False, False, False], [True, True, False, True], [False, False, False, False], [False, False, False, False]]
        self.assertEqual(shortest_path(m, (3,0), (0,0)), 7)