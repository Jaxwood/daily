import unittest
from problems.problem027 import well_formed


class TestProblem027(unittest.TestCase):

    def test_well_formed_returns_true(self):
        self.assertEqual(well_formed('([])[]({})'), True)

    def test_not_well_formed_returns_false(self):
        self.assertEqual(well_formed('([)]', ), False)
        self.assertEqual(well_formed('((()', ), False)
