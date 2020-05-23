import unittest
from problems.problem012 import stairs


class TestProblem010(unittest.TestCase):

    async def test_stairs(self):
        self.assertEqual(await stairs(4), 5)