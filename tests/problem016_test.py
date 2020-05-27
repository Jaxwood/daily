import unittest
from problems.problem016 import OrderLogger


class TestProblem016(unittest.TestCase):

    def test_stream(self):
        logger = OrderLogger()
        logger.record(1)
        logger.record(2)
        logger.record(3)
        self.assertEqual(logger.get_last(2), 2)