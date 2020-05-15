import unittest
from problems.problem005 import car, cons, cdr


class TestProblem003(unittest.TestCase):

    def test_car_pair_returnFirst(self):
        self.assertEqual(car(cons(3, 4)), 3)

    def test_cdr_pair_returnsLast(self):
        self.assertEqual(cdr(cons(3, 4)), 4)
