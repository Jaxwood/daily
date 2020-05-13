import unittest
from problems.problem002 import products, products2

class TestProblem002(unittest.TestCase):

    def test_products_example1_returnCorrectValues(self):
        self.assertEqual(products([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])
        self.assertEqual(products2([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_products_example2_returnCorrectValues(self):
        self.assertEqual(products([3, 2, 1]), [2, 3, 6])
        self.assertEqual(products2([3, 2, 1]), [2, 3, 6])

    def test_products_example3_returnCorrectValues(self):
        self.assertEqual(products([3, 2, 2, 1]), [4, 6, 6, 12])
        self.assertEqual(products2([3, 2, 2, 1]), [4, 6, 6, 12])