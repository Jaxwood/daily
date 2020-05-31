import unittest
from problems.problem019 import minimum_cost


class TestProblem019(unittest.TestCase):

    def test_minimum_cost(self):
        costs = [[(1,'red'),(2,'blue'),(3,'green')],
                 [(1,'red'),(2,'blue'),(4,'green')],
                 [(3,'red'),(6,'blue'),(8,'green')]]
        self.assertEqual(minimum_cost(costs), 6)