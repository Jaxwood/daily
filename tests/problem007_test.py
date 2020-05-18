import unittest
from problems.problem007 import unique_counter


class TestProblem007(unittest.TestCase):

    def test_unique_counter(self):
        self.assertEqual(unique_counter(111), 3)