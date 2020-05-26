import unittest
from problems.problem015 import stream


class TestProblem015(unittest.TestCase):

    def test_stream(self):
        self.assertEqual(stream(6), round(1/6, 3))