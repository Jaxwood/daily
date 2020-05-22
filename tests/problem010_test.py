import unittest
import asyncio
from problems.problem010 import schedule


class TestProblem010(unittest.TestCase):

    async def test_schedule(self):
        self.assertEqual(await schedule(1000, (lambda x: True)),  True)